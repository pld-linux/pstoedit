Summary:	Convert PostScript and PDF files into various vector-graphic formats
Summary(pl):	Konwerter PostScriptu i PDF do r�nych format�w wektorowych
Name:		pstoedit
Version:	3.40
Release:	3
License:	GPL
Group:		Applications/Graphics
Source0:	http://home.t-online.de/home/helga.glunz/wglunz/pstoedit/%{name}-%{version}.tar.gz
# Source0-md5:	5756c28eef3a11fe395248c5bf053556
Patch0:		%{name}-opt.patch
Patch1:		%{name}-no_pedantic.patch
Patch2:		%{name}-link.patch
Patch3:		%{name}-am18.patch
Patch4:		%{name}-fix.patch
URL:		http://home.t-online.de/home/helga.glunz/wglunz/pstoedit/
BuildRequires:	ImageMagick-c++-devel >= 1:6.2.4.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libEMF-devel
BuildRequires:	libplotter-devel >= 2.3
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel >= 3.0
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
pstoedit konwertuje pliki PostScript i PDF do wielu r�nych mniej lub
bardziej zdatnych do edycji format�w: gnuplot, idraw, xfig, tgif,
Tcl/Tk, HPGL, PIC, LaTeX2e, MetaPost, Sketch, KIllustrator, PDF, GNU
metafile, Java, DXF, Real3D, RenderMan, LightWave, Adobe Illustrator,
uproszczony PostScript i dowolny format jaki mog� zapisywa�
ghostscript lub GNU plotutils - np. Tektronix, CGM, r�ne formaty
rastrowe.

%package drv-lplot
Summary:	lplot plugin for pstoedit library
Summary(pl):	Wtyczka lplot dla biblioteki pstoedit
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description drv-lplot
lplot plugin for pstoedit library. It uses libplotter library.

%description drv-lplot -l pl
Wtyczka lplot dla biblioteki pstoedit. U�ywa biblioteki libplotter.

%package drv-magick
Summary:	magick plugin for pstoedit library
Summary(pl):	Wtyczka magick dla biblioteki pstoedit
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description drv-magick
magick plugin for pstoedit library. It uses Magick++ library.

%description drv-magick -l pl
Wtyczka magick (libplotter) dla biblioteki pstoedit. U�ywa biblioteki
Magick++.

%package drv-swf
Summary:	swf plugin for pstoedit library
Summary(pl):	Wtyczka swf dla biblioteki pstoedit
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description drv-swf
swf plugin for pstoedit library. It uses Ming library.

%description drv-swf -l pl
Wtyczka swf dla biblioteki pstoedit. U�ywa biblioteki Ming.

%package drv-wmf
Summary:	wmf plugin for pstoedit library
Summary(pl):	Wtyczka wmf dla biblioteki pstoedit
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description drv-wmf
wmf plugin for pstoedit library. It uses libEMF library.

%description drv-wmf -l pl
Wtyczka wmf dla biblioteki pstoedit. U�ywa biblioteki libEMF.

%package devel
Summary:	pstoedit library header files
Summary(pl):	Pliki nag��wkowe biblioteki pstoedit
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
pstoedit library header files.

%description devel -l pl
Pliki nag��wkowe biblioteki pstoedit.

%package static
Summary:	pstoedit static libraries
Summary(pl):	Biblioteki statyczne pstoedit
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
pstoedit static libraries.

%description static -l pl
Biblioteki statyczne pstoedit.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
# need to rebuild - supplied libtool is broken (relink and C++)
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	GS=/usr/bin/gs \
	--enable-static \
	--with-libemf-include=/usr/include/libEMF
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_aclocaldir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/pstoedit.1 $RPM_BUILD_ROOT%{_mandir}/man1

cp -af java $RPM_BUILD_ROOT%{_datadir}/pstoedit
rm -f $RPM_BUILD_ROOT%{_datadir}/pstoedit/java/*/{readme*,Makefile*} \
	$RPM_BUILD_ROOT%{_datadir}/pstoedit/java/Makefile* \
	$RPM_BUILD_ROOT%{_libdir}/pstoedit/lib*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/{readme.txt,*.htm} java/java1/readme_java1.txt java/java2/readme_java2.html
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
