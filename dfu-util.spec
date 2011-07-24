Summary:	Dfu-util device firmware upgrade utility
Summary(pl.UTF-8):	Narzędzie do aktualizacji oprogramowania urzadzeń USB
Name:		dfu-util
Version:	0.4
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://dfu-util.gnumonks.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	2cf466fabb881e8598fa02f286d3242c
URL:		http://wiki.openmoko.org/wiki/Dfu-util
BuildRequires:	libusb-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dfu-util is a program that implements the Host (PC) side of the USB
DFU (Universal Serial Bus Device Firmware Upgrade) protocol.

%description -l pl.UTF-8
dfu-util to program implementujący protokół USB DFU (Universal Serial
Bus Device Firmware Upgrade) po stronie hosta (PC).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/dfu-util
%{_mandir}/man?/*
