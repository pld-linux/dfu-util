Summary:	Dfu-util device firmware upgrade utility
Summary(pl.UTF-8):	Narzędzie do aktualizacji oprogramowania urzadzeń USB
Name:		dfu-util
Version:	0.11
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://dfu-util.sourceforge.net/releases/%{name}-%{version}.tar.gz
# Source0-md5:	31c983543a1fe8f03260ca4d56ad4f43
URL:		http://wiki.openmoko.org/wiki/Dfu-util
BuildRequires:	libusb-devel >= 1.0.0
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
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DEVICES.txt README TODO
%attr(755,root,root) %{_bindir}/dfu-prefix
%attr(755,root,root) %{_bindir}/dfu-suffix
%attr(755,root,root) %{_bindir}/dfu-util
%{_mandir}/man1/dfu-prefix.1*
%{_mandir}/man1/dfu-suffix.1*
%{_mandir}/man1/dfu-util.1*
