Summary:	Lua bindings to GObject libraries
Name:		lua-lgi
Version:	0.9.0
Release:	2
License:	BSD
Group:		Development/Libraries
Source0:	https://github.com/pavouk/lgi/archive/%{version}/lgi-%{version}.tar.gz
# Source0-md5:	cc433a597f23cfabdfc905c6c2cd3d7c
URL:		https://github.com/pavouk/lgi
BuildRequires:	glib2-devel
BuildRequires:	gobject-introspection-devel >= 0.10.8
BuildRequires:	libffi-devel
BuildRequires:	lua51-devel
BuildRequires:	pkgconfig
Requires:	lua51
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGI is gobject-introspection based dynamic Lua binding to GObject
based libraries. It allows using GObject-based libraries directly from
Lua.

%prep
%setup -q -n lgi-%{version}

%build
export CFLAGS="%{rpmcflags} `pkg-config --cflags lua51`"
export LDFLAGS="%{rpmldflags} `pkg-config --libs lua51`"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LUA_LIBDIR=%{_libdir}/lua/5.1 \
	LUA_SHAREDIR=%{_datadir}/lua/5.1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md docs/*.md
%dir %{_libdir}/lua/5.1/lgi
%attr(755,root,root) %{_libdir}/lua/5.1/lgi/corelgilua51.so
%{_datadir}/lua/5.1/lgi.lua
%{_datadir}/lua/5.1/lgi
