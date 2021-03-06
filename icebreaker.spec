Summary:	An addictive action-puzzle game involving bouncing penguins
Name:		icebreaker
Version:	1.9.9
Release:	0
%define 	isprerelease 0
%define		isdevelrelease 1
License:	GPL
Group:		Amusements/Games

%if %{isprerelease}
Source: 	icebreaker-%{version}-%{release}.tar.gz
%else
Source: 	icebreaker-%{version}.tar.gz
%endif

URL:		http://www.mattdm.org/icebreaker/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  SDL-devel, SDL_mixer-devel, /bin/awk, /bin/sed, /bin/grep

%if %{isprerelease}
%define extradescription *** Warning *** This is a prerelease build not meant for general public use.
%elseif %{isdevelrelease}
%define extradescription NOTE: This is a development release. Bug-testers only, please.
%endif

%description
IceBreaker is an action-puzzle game in which you must capture penguins from
an Antarctic iceberg so they can be shipped to Finland, where they are
essential to a secret plot for world domination. To earn the highest Geek
Cred, trap them in the smallest space in the shortest time while losing the
fewest lives. IceBreaker was inspired by (but is far from an exact clone of)
Jezzball by Dima Pavlovsky.
%{extradescription}

%prep
%if %{isprerelease}
%setup -q -n %{name}-%{version}-%{release}
%else
%setup -q
%endif

%build
make OPTIMIZE="$RPM_OPT_FLAGS" highscoredir=/var/lib/games prefix=/usr

%install
make install highscoredir=${RPM_BUILD_ROOT}/var/lib/games prefix=${RPM_BUILD_ROOT}/usr

mkdir -p ${RPM_BUILD_ROOT}/etc/X11/applnk/Games
install -m 644 icebreaker.desktop ${RPM_BUILD_ROOT}/etc/X11/applnk/Games

%post
touch %{_var}/lib/games/icebreaker.scores
chown games:games %{_var}/lib/games/icebreaker.scores
chmod 0664 %{_var}/lib/games/icebreaker.scores

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README README.themes TODO LICENSE ChangeLog
%attr(2755,root,games) %{_bindir}/icebreaker
/etc/X11/applnk/Games/icebreaker.desktop
%{_datadir}/icebreaker
%{_mandir}/man6/*
%attr(664,games,games) %ghost %{_var}/lib/games/icebreaker.scores

%changelog
* Thu Nov 16 2006 Matthew Miller <mattdm@mattdm.org>
- working towards 1.9.9 :)

* Fri May 31 2002 Matthew Miller <mattdm@mattdm.org>
- 1.9.6

* Mon May 27 2002 Matthew Miller <mattdm@mattdm.org>
- 1.9.5

* Thu May 23 2002 Matthew Miller <mattdm@mattdm.org>
- more complex makefile allows simpler specfile

* Tue May 21 2002 Matthew Miller <mattdm@mattdm.org>
- added themes docs

* Sun May 19 2002 Matthew Miller <mattdm@mattdm.org>
- inserted some convenience stuff to enable "make rpm" magic to work
- added "isprerelease" check. No one but me should care about this.

* Sun May 19 2002 Matthew Miller <mattdm@mattdm.org>
- 1.9.2

* Fri May 17 2002 Matthew Miller <mattdm@mattdm.org>
- REALLY add .ibt files for themes

* Mon May 13 2002 Matthew Miller <mattdm@mattdm.org>
- add .ibt files for themes

* Wed May 08 2002 Matthew Miller <mattdm@mattdm.org>
- 1.9.1

* Wed Aug 01 2001 Matthew Miller <mattdm@mattdm.org>
- 1.9.0

* Mon Jul 30 2001 Matthew Miller <mattdm@mattdm.org>
- 1.2.1

* Sat Jul 28 2001 Matthew Miller <mattdm@mattdm.org>
- 1.2

* Tue Jul 24 2001 Matthew Miller <mattdm@mattdm.org>
- move man page section 6

* Sun Jul 22 2001 Matthew Miller <mattdm@mattdm.org>
- 1.1

* Fri Jul 20 2001 Matthew Miller <mattdm@mattdm.org>
- borrowed idea of using post-script to create high score file
  from Mandrake RPM. That way, it doesn't have to be marked as a config
  file, and yet won't get zapped on upgrade.
- also, modified Makefile to cope with RPM_OPT_FLAGS, again as per
  Mandrake.

* Thu Jul 19 2001 Matthew Miller <mattdm@mattdm.org>
- added man page

* Tue Jul 18 2001 Matthew Miller <mattdm@mattdm.org>
- updated to 1.09

* Thu Oct 5 2000 Matthew Miller <mattdm@mattdm.org>
- looks good to me. one-point-oh

* Tue Oct 3 2000 Matthew Miller <mattdm@mattdm.org>
- updated to 0.995 
- better make process

* Mon Oct 2 2000 Matthew Miller <mattdm@mattdm.org>
- updated to 0.99 :)

* Mon Oct 2 2000 Matthew Miller <mattdm@mattdm.org>
- updated to 0.98

* Fri Sep 15 2000 Matthew Miller <mattdm@mattdm.org>
- first package
