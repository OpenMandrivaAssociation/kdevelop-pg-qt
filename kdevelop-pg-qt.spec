Summary: KDevelop-PG-Qt
Name: kdevelop-pg-qt
Version: 1.0.0
Release: %mkrel 1
Source0: http://fr2.rpmfind.net/linux/KDE/stable/%name/%version/src/%name-%version.tar.bz2
License: GPLv2+
Group: Development/Other
Url: http://techbase.kde.org/Development/KDevelop-PG-Qt_Introduction
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kdelibs4-devel
BuildRequires: bison flex

%description 
KDevelop-PG-Qt is a parser generator written in readable source-code and
generating readable source-code. Its syntax was inspirated by AntLR. It
implements the visitor-pattern and uses the Qt library. That is why it
is ideal to be used in Qt-/KDE-based applications like KDevelop.

%files
%defattr(-,root,root)
%{_kde_bindir}/kdev-pg-qt

#--------------------------------------------------------------------
%package devel
Summary: KDevelop-PG-Qt development files
Group: Development/Other
Requires: %name = %version

%description devel
This package contains development files of %name.

%files devel
%defattr(-,root,root)
%{_kde_includedir}/%{name}
%{_kde_libdir}/cmake/KDevelop-PG-Qt/KDevelop-PG-QtConfig.cmake
%{_kde_libdir}/cmake/KDevelop-PG-Qt/KDevelop-PG-QtConfigVersion.cmake
#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}
