Name: x11-font-encodings
Version: 1.0.2
Release: %mkrel 3
Summary: Xorg X11 font encodings
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/encodings-%{version}.tar.bz2
License: MIT
BuildArch: noarch

BuildRequires: x11-font-util	>= 1.0.1
BuildRequires: x11-util-macros	>= 1.1.5

Conflicts: xorg-x11-xfs <= 6.9.0
Requires(pre): mkfontdir

%description
This package contains the encodings that map to specific characters.

%prep
%setup -q -n encodings-%{version}

%build
%configure2_5x	\
   --x-includes=%{_includedir} \
   --x-libraries=%{_libdir} \
   --with-encodingsdir=%{_datadir}/fonts/encodings

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post
mkfontdir -n -e /usr/share/fonts/encodings /usr/share/fonts/encodings

%postun
mkfontdir -n -e /usr/share/fonts/encodings /usr/share/fonts/encodings

%files
%defattr(-,root,root)
%dir %{_datadir}/fonts/encodings
%{_datadir}/fonts/encodings/*
