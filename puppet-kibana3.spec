Name:           puppet-kibana3
Epoch:          1
Version:        XXX
Release:        XXX
Summary:        Installs and configures kibana3.
License:        Apache-2.0

URL:            https://github.com/thejandroman/puppet-kibana3

Source0:        https://github.com/thejandroman/puppet-kibana3/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet-git
Requires:       puppet-vcsrepo
Requires:       puppet-apache
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Installs and configures kibana3.

%prep
%setup -q -n %{name}-%{version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/kibana3/
cp -r %{buildroot}/%{_datadir}/openstack-puppet/modules/kibana3/



%files
%{_datadir}/openstack-puppet/modules/kibana3/


%changelog

