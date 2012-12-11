Name:           optipng
Version:        0.7.1
Release:        1
Summary:        A PNG optimizer and converter
Group:          Graphics
License:        zlib
URL:            http://optipng.sourceforge.net/
Source0:        http://surfnet.dl.sourceforge.net/sourceforge/optipng/optipng-%{version}.tar.gz
BuildRequires:  zlib-devel libpng-devel

%description
OptiPNG is a PNG optimizer that recompresses image files to a smaller size,
without losing any information. This program also converts external formats
(BMP, GIF, PNM; TIFF support is coming up) to optimized PNG, and performs PNG
integrity checks and corrections. 


%prep
%setup -q

%build
./configure -with-system-zlib -with-system-libpng
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
%makeinstall_std prefix=%{_prefix} man1dir=%{_mandir}/man1

%files
%doc README.txt LICENSE.txt doc/*
%{_bindir}/optipng
%{_mandir}/man1/optipng.*


%changelog
* Mon Mar 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.7.1-1
+ Revision: 787086
- removed old patch
- version update 0.7.1

* Sun Jun 05 2011 Funda Wang <fwang@mandriva.org> 0.6.5-1
+ Revision: 682751
- update to new version 0.6.5

* Sat Aug 07 2010 Emmanuel Andry <eandry@mandriva.org> 0.6.4-1mdv2011.0
+ Revision: 567376
- New version 0.6.4
- drop p1

* Sun Jul 26 2009 Emmanuel Andry <eandry@mandriva.org> 0.6.3-1mdv2010.0
+ Revision: 400437
- New version 0.6.3
- drop security patch
- add patch to fix string format error (reported upstream)

* Thu Mar 05 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.2-2mdv2009.1
+ Revision: 349137
- Apply 0.6.2.1 security patch

* Wed Nov 19 2008 Frederik Himpe <fhimpe@mandriva.org> 0.6.2-1mdv2009.1
+ Revision: 304470
- update to new version 0.6.2

* Mon Jul 21 2008 Funda Wang <fwang@mandriva.org> 0.6.1-1mdv2009.0
+ Revision: 239401
- New version 0.6.1
- rework systemlibs patch

* Thu May 22 2008 Frederik Himpe <fhimpe@mandriva.org> 0.5.5-2mdv2009.0
+ Revision: 210092
- Fix license short name
- Rebuild with new toolchain

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix man pages

