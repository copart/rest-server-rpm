Name:    rest-server
Version: 0.9.5
Release: 2%{?dist}
Summary: Rest Server is a high performance HTTP server that implements restic's REST backend API
URL:     https://restic.net
License: BSD

Requires(pre): shadow-utils
%{?systemd_requires}
BuildRequires: systemd
BuildRequires: golang
Source0: https://github.com/restic/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: rest-server.sysconfig
Source2: rest-server.service
Source3: rest-server.xml

%define debug_package %{nil}

%description
restic is a backup program that is fast, efficient and secure.

%prep
%autosetup

%build
go run build.go

%pre
getent group restsvr >/dev/null || groupadd -r restsvr
getent passwd restsvr >/dev/null || \
    useradd -r -g restsvr -d / -s /sbin/nologin \
    -c "Service account for rest-server (restic's REST backend API)" restsvr
exit 0

%install
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_prefix}/lib/firewalld/services
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 %{_builddir}/%{name}-%{version}/%{name} %{buildroot}%{_bindir}
install -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -m644 %{SOURCE2} %{buildroot}%{_unitdir}
install -m644 %{SOURCE3} %{buildroot}%{_prefix}/lib/firewalld/services/%{name}.xml

%files
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_prefix}/lib/firewalld/services/%{name}.xml
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%license LICENSE

%post
test -f %{_bindir}/firewall-cmd && %{_bindir}/firewall-cmd --reload --quiet

%changelog
* Wed Jan 10 2018 Steve Miller <copart@gmail.com> - 0.9.5-2
- Added config file to /etc/sysconfig
- Added systemd unit file
- Added firewalld service
- Added daemon user/group creation

* Tue Jan 09 2018 Steve Miller <copart@gmail.com> - 0.9.5-1
- Initial package build
