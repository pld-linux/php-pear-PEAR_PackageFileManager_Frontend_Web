%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	PackageFileManager_Frontend_Web
%define		_status		alpha
%define		_pearname	PEAR_PackageFileManager_Frontend_Web

Summary:	%{_pearname} - A Web GUI frontend for the PEAR_PackageFileManager2 class
Summary(pl.UTF-8):	%{_pearname} - Graficzny frontend WWW do klasy PEAR_PackageFileManger2
Name:		php-pear-%{_pearname}
Version:	0.6.0
Release:	1
License:	PHP License 3.01
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d5398fd5cdd72e2a2f1610d4c7b96466
URL:		http://pear.php.net/package/PEAR_PackageFileManager_Frontend_Web/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTML_QuickForm >= 3.2.6
Requires:	php-pear-HTML_QuickForm_Controller >= 1.0.6
Requires:	php-pear-HTML_Table >= 1.6.0
Requires:	php-pear-PEAR_PackageFileManager_Frontend >= 0.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(PHP/Compat.*)' 'pear(Text/Highlighter.*)'

%description
This package is a web frontend for the PEAR_PackageFileManager2 class.
It makes it easier for developers to create and maintain PEAR
package.xml files (versions 1.0 and 2.0).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza frontend WWW do klasy PEAR_PackageFileManager2.
Ułatwia programistom tworzenie i utrzymywanie plików package.xml (w
wersji 1.0 i 2.0).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}
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

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt docs/%{_pearname}/{ChangeLog,NEWS,examples}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PEAR/PackageFileManager/Frontend/Web
%{php_pear_dir}/PEAR/PackageFileManager/Frontend/Web.php
%{php_pear_dir}/PEAR/PackageFileManager/Frontend/Decorator
%{php_pear_dir}/data/PEAR_PackageFileManager_Frontend_Web
