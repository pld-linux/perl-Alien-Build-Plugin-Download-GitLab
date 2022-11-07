#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Alien
%define		pnam	Build-Plugin-Download-GitLab
Summary:	Alien::Build::Plugin::Download::GitLab - Alien::Build plugin to download from GitLab
Summary(pl.UTF-8):	Alien::Build::Plugin::Download::GitLab - wtyczka Alien::Build do pobierania z GitLaba
Name:		perl-Alien-Build-Plugin-Download-GitLab
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Alien/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ad1d815262ad7dd98b0a9b35ba2f05ef
URL:		https://metacpan.org/release/Alien-Build-Plugin-Download-GitLab
BuildRequires:	perl-devel >= 1:5.8.4
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Alien-Build
BuildRequires:	perl-Path-Tiny
BuildRequires:	perl-URI
BuildRequires:	perl-Test2-Suite >= 0.000121
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin is designed for downloading assets from a GitLab instance.

%description -l pl.UTF-8
Wtyczka stworzona do pobierania kodu z instancji GitLaba.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Alien/Build/Plugin/Download/GitLab.pm
%{_mandir}/man3/Alien::Build::Plugin::Download::GitLab.3pm*
