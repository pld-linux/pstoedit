# TODO: make Qt6 GUI in QT/PstoeditQtGui
Summary:	Convert PostScript and PDF files into various vector-graphic formats
Summary(pl.UTF-8):	Konwerter PostScriptu i PDF do różnych formatów wektorowych
Name:		pstoedit
Version:	4.01
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	https://downloads.sourceforge.net/pstoedit/%{name}-%{version}.tar.gz
# Source0-md5:	ac1e6b102cd94e9c954bd67ef984636d
Patch0:		pluginsdir.patch
Patch1:		imagemagick7.patch
URL:		http://www.pstoedit.com/
BuildRequires:	ImageMagick-c++-devel >= 6
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gd-devel
BuildRequires:	ghostscript
# TODO: change to texlive component when ready in PLD
BuildRequires:	latex2man
BuildRequires:	libEMF-devel
BuildRequires:	libplotter-devel >= 2.3
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2
BuildRequires:	libzip-devel
BuildRequires:	ming-devel
BuildRequires:	pkgconfig
BuildRequires:	texlive-format-pdflatex
BuildRequires:	texlive-xetex
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

%description -l pl.UTF-8
pstoedit konwertuje pliki PostScript i PDF do wielu różnych mniej lub
bardziej zdatnych do edycji formatów: gnuplot, idraw, xfig, tgif,
Tcl/Tk, HPGL, PIC, LaTeX2e, MetaPost, Sketch, KIllustrator, PDF, GNU
metafile, Java, DXF, Real3D, RenderMan, LightWave, Adobe Illustrator,
uproszczony PostScript i dowolny format jaki mogą zapisywać
ghostscript lub GNU plotutils - np. Tektronix, CGM, różne formaty
rastrowe.

%package devel
Summary:	pstoedit library header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki pstoedit
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gd-devel
Requires:	libstdc++-devel >= 6:4.7

%description devel
pstoedit library header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki pstoedit.

%package static
Summary:	pstoedit static library
Summary(pl.UTF-8):	Statyczna biblioteka pstoedit
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
pstoedit static library.

%description static -l pl.UTF-8
Statyczna biblioteka pstoedit.

%package drv-lplot
Summary:	lplot plugin for pstoedit library
Summary(pl.UTF-8):	Wtyczka lplot dla biblioteki pstoedit
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description drv-lplot
lplot plugin for pstoedit library. It uses libplotter library.

%description drv-lplot -l pl.UTF-8
Wtyczka lplot dla biblioteki pstoedit. Używa biblioteki libplotter.

%package drv-magick
Summary:	magick plugin for pstoedit library
Summary(pl.UTF-8):	Wtyczka magick dla biblioteki pstoedit
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description drv-magick
magick plugin for pstoedit library. It uses Magick++ library.

%description drv-magick -l pl.UTF-8
Wtyczka magick (libplotter) dla biblioteki pstoedit. Używa biblioteki
Magick++.

%package drv-pptx
Summary:	pptx plugin for pstoedit library
Summary(pl.UTF-8):	Wtyczka pptx dla biblioteki pstoedit
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description drv-pptx
pptx plugin for pstoedit library. It uses libzip library.

%description drv-pptx -l pl.UTF-8
Wtyczka pptx dla biblioteki pstoedit. Używa biblioteki libzip.

%package drv-swf
Summary:	swf plugin for pstoedit library
Summary(pl.UTF-8):	Wtyczka swf dla biblioteki pstoedit
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description drv-swf
swf plugin for pstoedit library. It uses Ming library.

%description drv-swf -l pl.UTF-8
Wtyczka swf dla biblioteki pstoedit. Używa biblioteki Ming.

%package drv-wmf
Summary:	wmf plugin for pstoedit library
Summary(pl.UTF-8):	Wtyczka wmf dla biblioteki pstoedit
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description drv-wmf
wmf plugin for pstoedit library. It uses libEMF library.

%description drv-wmf -l pl.UTF-8
Wtyczka wmf dla biblioteki pstoedit. Używa biblioteki libEMF.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
export CPPFLAGS="%{rpmcppflags} $(pkg-config --cflags libzip)"
%configure \
	GS=%{_bindir}/gs \
	--enable-static \
	--with-magick \
	--with-libemf-include=%{_includedir}/libEMF
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libpstoedit.la

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/pstoedit

cp -af contrib/java $RPM_BUILD_ROOT%{_datadir}/pstoedit
%{__rm} $RPM_BUILD_ROOT%{_datadir}/pstoedit/java/*/{readme*,Makefile*} \
	$RPM_BUILD_ROOT%{_datadir}/pstoedit/java/Makefile* \
	$RPM_BUILD_ROOT%{_libdir}/pstoedit/lib*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/{readme.txt,*.htm} contrib/java/java1/readme_java1.txt contrib/java/java2/readme_java2.html
%attr(755,root,root) %{_bindir}/pstoedit
%attr(755,root,root) %{_libdir}/libpstoedit.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpstoedit.so.0
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

%files drv-pptx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pstoedit/libp2edrvpptx.so*

%files drv-swf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pstoedit/libp2edrvswf.so*

%files drv-wmf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pstoedit/libp2edrvwmf.so*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpstoedit.so
%{_includedir}/pstoedit
%{_pkgconfigdir}/pstoedit.pc
%{_aclocaldir}/pstoedit.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libpstoedit.a
