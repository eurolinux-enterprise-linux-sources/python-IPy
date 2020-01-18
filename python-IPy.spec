%define oname IPy

# per fedora python packaging guidelines
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary:        Python module for handling IPv4 and IPv6 Addresses and Networks
Name:           python-%{oname}
Version:        0.75
Release:        5%{?dist}
URL:            https://github.com/haypo/python-ipy
Source0:        http://pypi.python.org/packages/source/I/IPy/IPy-%{version}.tar.gz
License:        BSD
Group:          System Environment/Libraries
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  python-devel
BuildArch:      noarch

%description
IPy is a Python module for handling IPv4 and IPv6 Addresses and Networks 
in a fashion similar to perl's Net::IP and friends. The IP class allows 
a comfortable parsing and handling for most notations in use for IPv4 
and IPv6 Addresses and Networks.

%prep
%setup -q -n %{oname}-%{version}

%build
CFLAGS="%{optflags}" %{_bindir}/python setup.py build

%check
make test

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog PKG-INFO README
%{python_sitelib}/%{oname}*


%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.75-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 25 2012 Matt Domsch <mdomsch@fedoraproject.org> - 0.75-4
- project URL moved to github

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.75-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.75-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Matt Domsch <mdomsch@fedoraproject.org> - 0.75-1
- Version 0.75 (2011-04-12)
 * IP('::/0').netmask() gives IP('::') instead of IP('0.0.0.0') (BZ#690625)
 * Fix tests for Python 3.1 and 3.2
 * ip.__nonzero__() and (ipa in ipb) return a bool instead of 0 or 1
 * IP('0.0.0.0/0') + IP('0.0.0.0/0') raises an error, fix written by Arfrever
 * Support Python 3: setup.py runs 2to3
 * Update the ranges for IPv6 IPs
 * Fix reverseName() and reverseNames() for IPv4 in IPv6 addresses
 * Drop support of Python < 2.5
 * Include examples and MANIFEST.in in source build (add them to MANIFEST.in)
 * Remove __rcsid__ constant from IPy module
 * Use xrange() instead of range()
 * Use isinstance(x, int) instead of type(x) == types.IntType
 * Prepare support of Python3 (use integer division: x // y)
 * Fix IP(long) constructor: ensure that the address is not too large
 * Constructor raise a TypeError if the type is not int, long, str or unicode
 * 223.0.0.0/8 is now public (belongs to APNIC)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.70-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jan 10 2010 Matt Domsch <mdomsch@fedoraproject.org> - 0.70-1
- Version 0.70 (2009-10-29)
  * New "major" version because it may break compatibility
  * Fix __cmp__(): IP('0.0.0.0/0') and IP('0.0.0.0') are not equal
  * Fix IP.net() of the network "::/0": "::" instead of "0.0.0.0".
    IPy 0.63 should fix this bug, but it wasn't.

* Sun Aug 30 2009 Matt Domsch <mdomsch@fedoraproject.org> - 0.63-1
- Fix formatting of "IPv4 in IPv6" network: IP('::ffff:192.168.10.0/120')

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.62-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.62-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.62-2
- Rebuild for Python 2.6

* Sat Nov 22 2008 Matt Domsch <mdomsch@fedoraproject.org> - 0.62-1
- new upstream version
  - Fix reverse DNS of IPv6 address: use ".ip6.arpa." suffix instead of deprecated ".ip6.int." suffix
  - Patch from Aras Vaichas allowing the [-1] operator to work with an IP object of size 1.

* Tue May 20 2008 Matt Domsch <matt@domsch.com> 0.60-1
- with assistance from  Mike Frisch
- 0.60

* Tue Jun 05 2007 Matt Domsch <matt@domsch.com> 0.53-2
- simple cleanups per Fedora package review, with thanks to Nigel Jones.

* Thu May 10 2007 Matt Domsch <matt@domsch.com> 0.53-1
- repackaged for Fedora

* Sat Jan 20 2007 David Walluck <walluck@mandriva.org> 0.52-1mdv2007.0
+ Revision: 110982
- 0.52

* Wed Dec 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0:0.51-2mdv2007.1
+ Revision: 96523
- Rebuild against new python

* Thu Nov 02 2006 David Walluck <walluck@mandriva.org> 0:0.51-1mdv2007.1
+ Revision: 75609
- 0.51

* Sun Oct 15 2006 David Walluck <walluck@mandriva.org> 0:0.42-3mdv2007.1
+ Revision: 65303
- sync with 2mdv
- Import python-IPy



* Sat Sep 16 2006 David Walluck <walluck@mandriva.com> 0:0.42-1mdv2007.0
- release
