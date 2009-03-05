Name:           optipng
Version:        0.6.2
Release:        %mkrel 2
Summary:        A PNG optimizer and converter
Group:          Graphics
License:        zlib
URL:            http://optipng.sourceforge.net/
Source0:        http://surfnet.dl.sourceforge.net/sourceforge/optipng/optipng-%{version}.tar.gz
Patch0:         optipng-0.6.1-use-system-libs.patch
# 0.6.2.1 security patch: http://optipng.sourceforge.net/
Patch1:		optipng-0.6.2.1.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  zlib-devel libpng-devel

%description
OptiPNG is a PNG optimizer that recompresses image files to a smaller size,
without losing any information. This program also converts external formats
(BMP, GIF, PNM; TIFF support is coming up) to optimized PNG, and performs PNG
integrity checks and corrections. 


%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
./configure -with-system-zlib -with-system-libpng
cd lib/pngxtern
make -f scripts/gcc.mak CFLAGS="%{optflags} %{ldflags}"
cd -
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}
%makeinstall_std prefix=%{_prefix} man1dir=%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt LICENSE.txt doc/*
%{_bindir}/optipng
%{_mandir}/man1/optipng.*
