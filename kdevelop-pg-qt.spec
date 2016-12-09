%define short_ver 2.0

Summary:	KDevelop-PG-Qt is a parser generator
Name:		kdevelop-pg-qt
Version:	%{short_ver}.0
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		http://techbase.kde.org/Development/KDevelop-PG-Qt_Introduction
Source0:	http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{short_ver}.tar.xz
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(ECM)

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
%{_includedir}/%{name}
%{_libdir}/cmake/KDevelop-PG-Qt/KDevelop-PG-QtConfig.cmake
%{_libdir}/cmake/KDevelop-PG-Qt/KDevelop-PG-QtConfigVersion.cmake
#--------------------------------------------------------------------

%prep
%setup -qn %{name}-%{short_ver}
%apply_patches

%build
export CXX='%__cxx -std=c++11'
%cmake_kde5
%ninja

%install
%ninja_install -C build

