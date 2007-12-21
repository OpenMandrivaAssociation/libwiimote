%define name libwiimote
%define version 0.4
%define release %mkrel 1

%define lib_major 0
%define cname cwiimote
%define lib_name %mklibname %{cname} %{lib_major}
%define devel_name %mklibname %{cname} -d

Summary: Simple Wiimote Library for Linux
Name: %{name}
Version: %{version}
Release: %{release}
Source0:  http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
License: GPL
Group: System/Kernel and hardware
Url: http://libwiimote.sourceforge.net/
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
autoreconf

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std libwiimote_includedir=%{_includedir}/lib%{cname}

%clean
rm -rf %{buildroot}

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%doc AUTHORS NEWS README TODO
%{_libdir}/lib%{cname}.so.%{lib_major}*

%files -n %{devel_name}
%dir %{_includedir}/lib%{cname}
%{_includedir}/lib%{cname}/*.h
%{_libdir}/lib%{cname}.a
