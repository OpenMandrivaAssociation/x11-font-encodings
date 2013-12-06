Name: x11-font-encodings
Version: 1.0.4
Release: 7
Summary: Xorg X11 font encodings
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/encodings-%{version}.tar.bz2
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
./configure --prefix=/usr \
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


%changelog
* Wed Apr 13 2011 Funda Wang <fwang@mandriva.org> 1.0.4-2mdv2011.0
+ Revision: 653113
- fix post script req

* Sat Oct 30 2010 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 590413
- new release

* Wed Jan 13 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.3-1mdv2010.1
+ Revision: 490685
- License is Public Domain, not MIT
- New version: 1.0.3

* Tue Jan 06 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-4mdv2009.1
+ Revision: 325503
- rebuilt due to package loss?

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2009.0
+ Revision: 225990
- rebuild
- fix no-buildroot-tag

* Tue Jan 22 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-2mdv2008.1
+ Revision: 156530
- Updated BuildRequires and resubmit package.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 55489
- use Requires(pre) instread of PreReq
- update description
- update to the latest upstream version


* Thu Mar 01 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.0-6mdv2007.0
+ Revision: 130447
- Re-generate encodings.dir when the package is installed (#29020)

* Fri Nov 17 2006 Pablo Saratxaga <pablo@mandriva.com> 1.0.0-5mdv2007.1
+ Revision: 85225
- removed wrong postinstall script (it was deleting the needed encodings.dir)

* Sat Aug 05 2006 Helio Chissini de Castro <helio@mandriva.com> 1.0.0-4mdv2007.0
+ Revision: 52705
- Encondings should go to new path too

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - increment release
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

