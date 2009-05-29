%define upstream_name    autobox
%define upstream_version 2.55

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Call methods on native types
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz


BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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


