Summary:	Convert PostScript and PDF files into various vector-graphic formats
Summary(pl):	Konwerter PostScriptu i PDF do ró¿nych formatów wektorowych
Name:		pstoedit
Version:	3.33
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://home.t-online.de/home/helga.glunz/wglunz/pstoedit/%{name}-%{version}.tar.gz
# Source0-md5:	6a671ef165bf7d1611a2ad3f0499ff5b
Source1:	http://autotrace.sourceforge.net/tools/pstoedit.m4
# NoSource1-md5: 6d3384b46da54a8ccdb9d47254820b89
Patch0:		%{name}-opt.patch
Patch1:		%{name}-no_pedantic.patch
URL:		http://home.t-online.de/home/helga.glunz/wglunz/pstoedit/
BuildRequires:	ImageMagick-c++-devel >= 5.4.8
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libEMF-devel
BuildRequires:	libplotter-devel >= 2.3
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	ming-devel
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

%package drv-lplot
Summary:	lplot plugin for pstoedit library
Summary(pl):	Wtyczka lplot dla biblioteki pstoedit
Group:		Libraries
Requires:	%{name} = %{version}

%description drv-lplot
lplot plugin for pstoedit library. It uses libplotter library.

%description drv-lplot -l pl
Wtyczka lplot dla biblioteki pstoedit. U¿ywa biblioteki libplotter.

%package drv-magick
Summary:	magick plugin for pstoedit library
Summary(pl):	Wtyczka magick dla biblioteki pstoedit
Group:		Libraries
Requires:	%{name} = %{version}

%description drv-magick
magick plugin for pstoedit library. It uses Magick++ library.

%description drv-magick -l pl
Wtyczka magick (libplotter) dla biblioteki pstoedit. U¿ywa biblioteki
Magick++.

%package drv-swf
Summary:	swf plugin for pstoedit library
Summary(pl):	Wtyczka swf dla biblioteki pstoedit
Group:		Libraries
Requires:	%{name} = %{version}

%description drv-swf
swf plugin for pstoedit library. It uses Ming library.

%description drv-swf -l pl
Wtyczka swf dla biblioteki pstoedit. U¿ywa biblioteki Ming.

%package drv-wmf
Summary:	wmf plugin for pstoedit library
Summary(pl):	Wtyczka wmf dla biblioteki pstoedit
Group:		Libraries
Requires:	%{name} = %{version}

%description drv-wmf
wmf plugin for pstoedit library. It uses libEMF library.

%description drv-wmf -l pl
Wtyczka wmf dla biblioteki pstoedit. U¿ywa biblioteki libEMF.

%package devel
Summary:	pstoedit library header files
Summary(pl):	Pliki nag³ówkowe biblioteki pstoedit
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
pstoedit library header files.

%description devel -l pl
Pliki nag³ówkowe biblioteki pstoedit.

%package static
Summary:	pstoedit static libraries
Summary(pl):	Biblioteki statyczne pstoedit
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
pstoedit static libraries.

%description static -l pl
Biblioteki statyczne pstoedit.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
# need to rebuild - supplied libtool is broken (relink and C++)
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

CPPFLAGS="-I/usr/X11R6/include -I/usr/X11R6/include/X11"
%configure \
	--with-libemf-include=/usr/include/libEMF
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_aclocaldir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/pstoedit.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_aclocaldir}

cp -af java $RPM_BUILD_ROOT%{_datadir}/pstoedit
rm -f $RPM_BUILD_ROOT%{_datadir}/pstoedit/java/*/readme*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.txt java/java1/readme_java1.txt *.htm java/java2/readme_java2.html
%attr(755,root,root) %{_bindir}/pstoedit
%attr(755,root,root) %{_libdir}/libpstoedit.so.*.*
%dir %{_libdir}/pstoedit
%attr(755,root,root) %{_libdir}/pstoedit/libp2edrvstd.so*
%{_datadir}/pstoedit
%{_mandir}/man1/pstoedit.1*

%files drv-lplot
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pstoedit/libp2edrvlplot.so*

%files drv-magick
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pstoedit/libp2edrvmagick++.so*

%files drv-swf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pstoedit/libp2edrvswf.so*

%files drv-wmf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pstoedit/libp2edrvwmf.so*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pstoedit-config
%attr(755,root,root) %{_libdir}/libpstoedit.so
%{_libdir}/libpstoedit.la
%{_includedir}/pstoedit
%{_pkgconfigdir}/*.pc
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libpstoedit.a
