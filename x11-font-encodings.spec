Name: x11-font-encodings
Version: 1.0.4
Release: 10
Summary: Xorg X11 font encodings
Group: Development/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/font/encodings-%{version}.tar.bz2
License: Public Domain
BuildArch: noarch

BuildRequires: x11-font-util	>= 1.0.1
BuildRequires: x11-util-macros	>= 1.1.5

Conflicts: xorg-x11-xfs <= 6.9.0
Requires(post,postun): mkfontdir

%description
This package contains the encodings that map to specific characters.

%prep
%setup -q -n encodings-%{version}

%build
%configure --with-encodingsdir=%{_datadir}/fonts/encodings
%make

%install
%makeinstall_std

%post
mkfontdir -n -e /usr/share/fonts/encodings /usr/share/fonts/encodings

%postun
mkfontdir -n -e /usr/share/fonts/encodings /usr/share/fonts/encodings

%files
%dir %{_datadir}/fonts/encodings
%{_datadir}/fonts/encodings/*


