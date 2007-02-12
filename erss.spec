Summary:	RSS reader using EFL
Summary(pl.UTF-8):   Czytnik RSS używający EFL
Name:		erss
Version:	0.0.2
%define	_snap	20050701
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Applications
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/misc/%{name}-%{_snap}.tar.gz
# Source0-md5:	629fa11611df863ae9d54d31265c4a64
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esmart-devel
BuildRequires:	etox-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RSS reader using EFL.

%description -l pl.UTF-8
Czytnik RSS używający EFL.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
