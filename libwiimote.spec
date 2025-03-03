%define name libwiimote
%define version 0.4
%define release %mkrel 6

%define lib_major 0
%define cname cwiimote
%define lib_name %mklibname %{cname} %{lib_major}
%define devel_name %mklibname %{cname} -d

Summary: Simple Wiimote Library for Linux
Name: %{name}
Version: %{version}
Release: %{release}
Source0:  http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
Patch0: libwiimote-0.4-bluez4.patch
Patch1: libwiimote-0.4-link.patch
License: GPL
Group: System/Kernel and hardware
Url: https://libwiimote.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: bluez-devel

%description
Libwiimote is a C-library that provides a simple API for communicating
with the Nintendo Wii Remote (aka. wiimote) on a Linux system. The
goal of this library is to be a complete and easy to use framework for
interfacing applications with the wiimote.

%package -n	%{lib_name}
Summary:	%{cname} library
Group:		System/Libraries

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with the %{cname} library.

%package -n	%{devel_name}
Summary:	Development headers and libraries for %{cname}
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	%{cname}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devel_name}
This package contains the header files and libraries needed for
developing programs using the %{cname} library.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
export CFLAGS="%{optflags} -fPIC"
autoreconf -fi
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std libwiimote_includedir=%{_includedir}/lib%{cname}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files -n %{lib_name}
%doc AUTHORS NEWS README TODO
%{_libdir}/lib%{cname}.so.%{lib_major}*

%files -n %{devel_name}
%dir %{_includedir}/lib%{cname}
%{_includedir}/lib%{cname}/*.h
%{_libdir}/lib%{cname}.a


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4-6mdv2011.0
+ Revision: 609786
- rebuild

* Sun Feb 21 2010 Funda Wang <fwang@mandriva.org> 0.4-5mdv2010.1
+ Revision: 509123
- bump rel
- fix build with latest bluez

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.4-1mdv2008.1
+ Revision: 136531
- build with -fPIC
- initial libwiimote package
- create libwiimote

