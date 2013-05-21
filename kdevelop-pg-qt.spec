Summary:	KDevelop-PG-Qt is a parser generator
Name:		kdevelop-pg-qt
Version:	1.0.0
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		http://techbase.kde.org/Development/KDevelop-PG-Qt_Introduction
Source0:	http://fr2.rpmfind.net/linux/KDE/stable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	kdelibs4-devel

%description
KDevelop-PG-Qt is a parser generator written in readable source-code and
generating readable source-code. Its syntax was inspirated by AntLR. It
implements the visitor-pattern and uses the Qt library. That is why it
is ideal to be used in Qt-/KDE-based applications like KDevelop.

%files
%{_kde_bindir}/kdev-pg-qt

#--------------------------------------------------------------------
%package devel
Summary:	KDevelop-PG-Qt development files
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains development files of %{name}.

%files devel
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
%makeinstall_std -C build

