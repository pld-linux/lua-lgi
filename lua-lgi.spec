Summary:	Lua bindings to GObject libraries
Summary(pl.UTF-8):	Wiązania języka Lua do bibliotek GObject
Name:		lua-lgi
Version:	0.9.2
Release:	1
License:	MIT
Group:		Development/Libraries
#Source0Download: https://github.com/pavouk/lgi/releases
Source0:	https://github.com/pavouk/lgi/archive/%{version}/lgi-%{version}.tar.gz
# Source0-md5:	ad5d2e7a4427069f926f2ca472a5fe6d
URL:		https://github.com/pavouk/lgi
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gobject-introspection-devel >= 0.10.8
BuildRequires:	libffi-devel >= 3.0
BuildRequires:	lua51-devel >= 5.1
BuildRequires:	pkgconfig
Requires:	lua51 >= 5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGI is gobject-introspection based dynamic Lua binding to GObject
based libraries. It allows using GObject-based libraries directly from
Lua.

%description -l pl.UTF-8
LGI to oparte na bibliotece gobject-introspection dynamiczne wiązanie
języka Lua do bibliotek opartych na szkielecie GObject. Pozwala na
używanie bibliotek opartych na GObject bezpośrednio z języka Lua.

%prep
%setup -q -n lgi-%{version}

%build
LIBS="$(pkg-config --libs lua51)" \
%{__make} \
	CC="%{__cc}" \
	COPTFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	LUA=lua51 \
	LUA_CFLAGS="$(pkg-config --cflags lua51)"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LUA_LIBDIR=%{_libdir}/lua/5.1 \
	LUA_SHAREDIR=%{_datadir}/lua/5.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md docs/*.md
%dir %{_libdir}/lua/5.1/lgi
%attr(755,root,root) %{_libdir}/lua/5.1/lgi/corelgilua51.so
%{_datadir}/lua/5.1/lgi.lua
%{_datadir}/lua/5.1/lgi
