%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Services_Atlassian_Crowd
Summary:	%{_pearname} - a package to use Atlassian Crowd from PHP
Summary(pl.UTF-8):	%{_pearname} - pakiet do korzystania z Atlassian Crowd
Name:		php-pear-%{_pearname}
Version:	0.9.5
Release:	2
License:	Apache
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	13356fe0151469a3c4ed587bd03f1f29
URL:		http://pear.php.net/package/Services_Atlassian_Crowd/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-soap
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crowd is a web-based single sign-on (SSO) tool that simplifies
application provisioning and identity management.

This package is derived from the PHP Client Library for Atlassian
Crowd class written by Infinite Campus, Inc.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Crowd to oparte na www narzędzie typu single sign-on (SSO)
upraszczające zarządzanie bezpieczeństwem aplikacji oraz tożsamościami
użytkowników.

Pakiet ten oparty jest na bibliotece klienckiej Atlassian Crowd
napisanej przez firmę Infinite Campus, Inc.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/Atlassian

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_Atlassian_Crowd
