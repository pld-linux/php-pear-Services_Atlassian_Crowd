%define		_status		beta
%define		_pearname	Services_Atlassian_Crowd
Summary:	%{_pearname} - a package to use Atlassian Crowd from PHP
Summary(pl.UTF-8):	%{_pearname} - pakiet do korzystania z Atlassian Crowd
Name:		php-pear-%{_pearname}
Version:	0.9.5
Release:	4
License:	Apache
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	13356fe0151469a3c4ed587bd03f1f29
URL:		http://pear.php.net/package/Services_Atlassian_Crowd/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(soap)
Requires:	php-pear
Obsoletes:	php-pear-Services_Atlassian_Crowd-tests
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
