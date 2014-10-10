%define upstream_name    Net-LDAP-Server
%define upstream_version 0.43

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	LDAP server side protocol handling
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Convert::ASN1)
BuildRequires:	perl(Net::LDAP)

BuildArch:	noarch

%description
LDAP server side protocol handling.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changelog README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.430.0-1mdv2011.0
+ Revision: 682137
- update to new version 0.43

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.420.0-2
+ Revision: 655140
- rebuild for updated spec-helper

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.420.0-1mdv2011.0
+ Revision: 461335
- update to 0.42

* Sun Jul 19 2009 Buchan Milne <bgmilne@mandriva.org> 0.4-1mdv2010.0
+ Revision: 397925
- import perl-Net-LDAP-Server


* Sun Jul 19 2009 Buchan Milne <bgmilne@mandriva.org> 0.4-1mdv
- initial mdv release, generated with cpan2dist

