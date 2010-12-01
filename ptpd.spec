Name: ptpd
Version: 1.1.0	
Release: 1%{?dist}
Summary: PTPd implements the Precision Time protocol (PTP) as defined by the IEEE 1588

Group: System Environment/Daemons
License: BSD
URL: http://ptpd.sourceforge.net/
Source0: http://sourceforge.net/projects/ptpd/files/ptpd/1.1.0/ptpd-1.1.0.tar.gz	
Source1: http://www2.xp-dev.com/sc/browse/105044/1.1.0-1/ptpd-etc-patch.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
The PTP daemon (PTPd) implements the Precision Time protocol (PTP) as defined 
by the relevant IEEE 1588 standard. PTP was developed to provide very precise
time coordination of LAN connected computers.

PTPd is a complete implementation of the IEEE 1588 specification for a standard 
(non-boundary) clock. PTPd has been tested with and is known to work properly 
with other IEEE 1588 implementations.

PTPd can run on most 32-bit or 64-bit, little- or big-endian processors. It 
does not require an FPU, so it is great for embedded processors.

%prep
# extract first source implicitly and add in fedora init script and sysconfig
%setup -a 1

%build
cd src
CFLAGS="%{optflags}" make ptpd


%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}%{_bindir}
mkdir -p  %{buildroot}%{_initrddir}
mkdir -p  %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_mandir}/man8/
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-%{version}
cp -p etc/init.d/ptpd %{buildroot}/%{_initddir}/ptpd
cp -p etc/sysconfig/ptpd %{buildroot}/%{_sysconfdir}/sysconfig
cp -p src/ptpd %{buildroot}/%{_bindir}
cp -p src/ptpd.8 %{buildroot}/%{_mandir}/man8/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sysconfdir}/*
%{_initrddir}/*
%{_bindir}/*
%doc COPYRIGHT ChangeLog README RELEASE_NOTES
%{_mandir}/man8/*


%changelog
* Wed Dec 01 2010 Jon Kent <jon.kent at, gmail.com> 1.1.0-1
- Cleaned up description
- Moved docs to use %doc tag
- Cleaned up %build section
- Cleaned up the src and init/sysconfig extraction
* Sun Nov 21 2010 Jon Kent <jon.kent at, gmail.com> 1.1.0-1
- First release of ptpd for Fedora
