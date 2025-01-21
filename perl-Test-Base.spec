#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Test-Base
Version  : 0.89
Release  : 40
URL      : https://cpan.metacpan.org/authors/id/I/IN/INGY/Test-Base-0.89.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IN/INGY/Test-Base-0.89.tar.gz
Summary  : 'A Data Driven Testing Framework'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Base-license = %{version}-%{release}
Requires: perl-Test-Base-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Algorithm::Diff)
BuildRequires : perl(Spiffy)
BuildRequires : perl(Test::More)
BuildRequires : perl(Text::Diff)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Test::Base - A Data Driven Testing Framework
SYNOPSIS
A new test module:
# lib/MyProject/Test.pm
package MyProject::Test;
use Test::Base -Base;

use MyProject;

package MyProject::Test::Filter;
use Test::Base::Filter -base;

sub my_filter {
return MyProject->do_something(shift);
}

%package dev
Summary: dev components for the perl-Test-Base package.
Group: Development
Provides: perl-Test-Base-devel = %{version}-%{release}
Requires: perl-Test-Base = %{version}-%{release}

%description dev
dev components for the perl-Test-Base package.


%package license
Summary: license components for the perl-Test-Base package.
Group: Default

%description license
license components for the perl-Test-Base package.


%package perl
Summary: perl components for the perl-Test-Base package.
Group: Default
Requires: perl-Test-Base = %{version}-%{release}

%description perl
perl components for the perl-Test-Base package.


%prep
%setup -q -n Test-Base-0.89
cd %{_builddir}/Test-Base-0.89

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Base
cp %{_builddir}/Test-Base-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Base/883758993cc9a404b18936c49f4c6f4db25e763a || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Base.3
/usr/share/man/man3/Test::Base::Filter.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Base/883758993cc9a404b18936c49f4c6f4db25e763a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
