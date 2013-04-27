%define upstream_name    autobox
%define upstream_version 2.77
%define debug_package          %{nil}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	1

Summary:    Call methods on native types
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Scope::Guard)
BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Provides: perl(autobox)

%description
The autobox pragma allows methods to be called on integers, floats,
strings, arrays, hashes, and code references in exactly the same manner as
blessed references.

The autoboxing is transparent: boxed values are not blessed into their
(user-defined) implementation class (unless the method elects to bestow
such a blessing) - they simply use its methods as though they are.

The classes (packages) into which the native types are boxed are fully
configurable. By default, a method invoked on a non-object is assumed to be
defined in a class whose name corresponds to the 'ref()' type of that value
- or SCALAR if the value is a non-reference.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.730.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Mar 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.730.0-1
+ Revision: 644730
- update to new version 2.73

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.720.0-1
+ Revision: 634205
- update to new version 2.72

* Sat Oct 16 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.710.0-1mdv2011.0
+ Revision: 585983
- new upstream version

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.700.0-2mdv2011.0
+ Revision: 555224
- rebuild

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 2.700.0-1mdv2010.1
+ Revision: 526461
- update to 2.70

* Fri May 29 2009 Jérôme Quelin <jquelin@mandriva.org> 2.550.0-1mdv2010.0
+ Revision: 380980
- adding missing buildrequires
- adding provides that gets filtered
- import perl-autobox


* Fri May 29 2009 cpan2dist 2.55-1mdv
- initial mdv release, generated with cpan2dist

