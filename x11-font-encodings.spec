Name: x11-font-encodings
Version: 1.1.0
Release: 1
Summary: Xorg X11 font encodings
Group: Development/X11
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/font/encodings-%{version}.tar.xz
License: Public Domain
BuildArch: noarch
BuildRequires: pkgconfig(fontutil) >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.1.5
Requires(post,postun): mkfontscale

%description
This package contains the encodings that map to specific characters.

%prep
%autosetup -n encodings-%{version} -p1

%build
%configure --with-encodingsdir=%{_datadir}/fonts/encodings
%make_build

%install
%make_install

%post
mkfontdir -n -e /usr/share/fonts/encodings /usr/share/fonts/encodings

%postun
mkfontdir -n -e /usr/share/fonts/encodings /usr/share/fonts/encodings

%files
%dir %{_datadir}/fonts/encodings
%{_datadir}/fonts/encodings/*
