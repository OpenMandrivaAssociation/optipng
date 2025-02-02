Name:           optipng
Version:        0.7.8
Release:        1
Summary:        A PNG optimizer and converter
Group:          Graphics
License:        zlib
URL:            https://optipng.sourceforge.net/
Source0:        http://sourceforge.net/projects/optipng/files/OptiPNG/optipng-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(zlib) 
BuildRequires:  pkgconfig(libpng)

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
