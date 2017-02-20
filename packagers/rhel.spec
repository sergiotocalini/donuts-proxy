Summary:                 Donuts Proxy.
Name:                    donuts-proxy
Version:                 1.0.0
Release:                 1%{?dist}
License:                 GPLv3
URL:                     https://github.com/sergiotocalini/donuts-proxy
Source0:                 https://github.com/sergiotocalini/donuts-proxy/download/donuts_ddns-%{version}.tar.gz
Group:                   Development/Languages
BuildArch:               noarch
Requires:                python26
Requires:                python26-requests
Requires:                python26-PyYAML
Requires:                python26-setuptools

%description
Donuts Proxy is a proxy to balance between public slave DNS servers.

%clean

%prep
%setup -q -n donuts_proxy-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add donuts-proxy
/sbin/chkconfig --level 345 donuts-proxy on

%files
%defattr(-,root,root,-)
                        /etc/donuts
                        /etc/init.d/donuts*
                        %{python_sitelib}/donuts_proxy
			%{python_sitelib}/donuts_proxy-*-py2.*.egg-info
%attr(755,-,-)          /usr/bin

%changelog
* Sat Jul 23 2016 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 1.0.1
- Initial spec with donuts_proxy-1.0.0 version.
