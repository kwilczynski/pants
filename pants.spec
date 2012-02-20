%define major 0
%define minor 0
%define patch 0

Summary: Make sure you're wearing pants when you go multiuser. 
Name: pants
Version: %{major}.%{minor}.%{patch}
Release: 2
Copyright: GNU General Public Licence
URL: http://vergenet.net/~conrad/scripts/pants.html
Packager: Horms <horms@vergenet.net>
Group: Applications/System
Source0: ftp://ftp.cse.unsw.edu.au/pub/users/conradp/scripts/pants
BuildRoot: /var/tmp/%name-%{version}-root
Provides: %{name}-%{version}

%description
Make sure you're wearing pants when you go multiuser. 

%prep

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/etc/rc.d/init.d/

install -m744 ${RPM_SOURCE_DIR}/pants \
  ${RPM_BUILD_ROOT}/etc/rc.d/init.d/pants

%clean
rm -rf $RPM_BUILD_DIR/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add pants

%postun

%preun
/sbin/chkconfig --del pants

%files 
/etc/rc.d/init.d/pants


%changelog
* Mon Apr 17 2000 Horms <horms@vergenet.net>
- created for version 0.31.7
