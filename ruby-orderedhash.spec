%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
Summary:	Ordered Hash for Ruby
Summary(pl):	Uporz±dkowane hasze dla jêzyka Ruby
Name:		ruby-OrderedHash
Version:	1.2005.8.16
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://simplypowerful.1984.cz/orderedhash/%{version}/orderedhash.tgz
# Source0-md5:	eac01684b6fb3c4c56a69e8acfebb704
URL:	http://simplypowerful.1984.cz/orderedhash/1.2005.8.16/doc/
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hash with preserved order (like Array in php)

%description -l pl
Hasze z zachowan± kolejno¶ci± (podobne do Array w php).

%prep
%setup -q -c

%build
rdoc -o rdoc *.rb
rdoc --ri -o ri *.rb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

cp -a *.rb $RPM_BUILD_ROOT/%{ruby_rubylibdir}
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/*.rb
%{ruby_ridir}/*
