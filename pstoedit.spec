Summary:	Convert PostScript and PDF files into various vector-graphic formats
Summary(pl):	Konwerter PostScriptu i PDF do ró¿nych formatów wektorowych
Name:		pstoedit
Version:	3.30
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://home.t-online.de/home/helga.glunz/wglunz/pstoedit/%{name}_3_30.zip
URL:		http://home.t-online.de/home/helga.glunz/wglunz/pstoedit/
BuildRequires:	unzip
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRequires:	libpng-devel
BuildRequires:	libplotter-devel >= 2.3
Requires:	ghostscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pstoedit converts PostScript and PDF files into a wide variety of
editable (and not-so-editable) formats: gnuplot, idraw, xfig, tgif,
Tcl/Tk, HPGL, PIC, LaTeX2e, MetaPost, Sketch, KIllustrator, PDF, GNU
metafile, Java, DXF, Real3D, RenderMan, LightWave, Adobe Illustrator,
simplified PostScript, and any format that Ghostscript or the GNU
plotting utilities can output, such as Tektronix, CGM, and various
bitmap formats.

%description -l pl
pstoedit konwertuje pliki PostScript i PDF do wielu ró¿nych mniej lub
bardziej zdatnych do edycji formatów: gnuplot, idraw, xfig, tgif,
Tcl/Tk, HPGL, PIC, LaTeX2e, MetaPost, Sketch, KIllustrator, PDF, GNU
metafile, Java, DXF, Real3D, RenderMan, LightWave, Adobe Illustrator,
uproszczony PostScript i dowolny format jaki mog± zapisywaæ
ghostscript lub GNU plotutils - np. Tektronix, CGM, ró¿ne formaty
rastrowe.

%prep
%setup -q -n %{name}_%{version}

%build
(cd config
autoconf
%configure --libdir=%{_datadir}/pstoedit
)
(cd src
cat Makefile | sed 's/-g -O2/%{rpmcflags}}/g' > Makefile.tmp
mv -f Makefile.tmp Makefile
%{__make}
)

%install
rm -rf $RPM_BUILD_ROOT
(cd src
%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	libdir=$RPM_BUILD_ROOT%{_datadir}/pstoedit \
	mandir=$RPM_BUILD_ROOT%{_mandir}
)
cp -af java $RPM_BUILD_ROOT%{_datadir}/pstoedit
rm -f $RPM_BUILD_ROOT%{_datadir}/pstoedit/java/*/readme*
cp -af misc/* $RPM_BUILD_ROOT%{_datadir}/pstoedit

gzip -9nf readme.txt java/java1/readme_java1.txt

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(644,root,root,755)
%doc *.gz java/java1/*.gz *.htm java/java2/readme_java2.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/pstoedit
%{_mandir}/man1/*
