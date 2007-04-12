Name:           optipng
Version:        0.5.5
Release:        %mkrel 1
Summary:        A PNG optimizer and converter

Group:          Graphics
License:        zlib/libpng
URL:            http://optipng.sourceforge.net/
Source0:        http://surfnet.dl.sourceforge.net/sourceforge/optipng/optipng-%{version}.tar.bz2
Patch0:         optipng-0.5.4-makefile-externlibs.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  zlib-devel libpng-devel

%description
OptiPNG is a PNG optimizer that recompresses image files to a smaller size,
without losing any information. This program also converts external formats
(BMP, GIF, PNM; TIFF support is coming up) to optimized PNG, and performs PNG
integrity checks and corrections. 


%prep
%setup -q
%patch0 -p1

%define makefile gcc.mak

%build
cd src/
%make -f scripts/%{makefile} %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"\
                                            LDFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
cd src/
%make -f scripts/%{makefile} install DESTDIR="$RPM_BUILD_ROOT"\
                                    prefix="%{_prefix}" \
                                    man1dir="%{_mandir}/man1"


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.txt LICENSE.txt doc/*
%{_bindir}/optipng
%{_mandir}/man1/optipng.1.bz2



