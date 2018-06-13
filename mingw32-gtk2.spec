#
# spec file for package mingw32-gtk2
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define __strip %{_mingw32_strip}
%define __objdump %{_mingw32_objdump}
%define _use_internal_dependency_generator 0
%define __find_requires %{_mingw32_findrequires}
%define __find_provides %{_mingw32_findprovides}
%define __os_install_post %{_mingw32_debug_install_post} \
                          %{_mingw32_install_post}

Name:           mingw32-gtk2
Version:        2.24.22
Release:        0
Summary:        Library for Creation of Graphical User Interfaces (version 2)
License:        LGPL-2.1+
Group:          System/Libraries

Url:            http://www.gtk.org/
Source:         http://download.gnome.org/sources/gtk+/2.24/gtk+-%{version}.tar.xz
                # build mingw64 fix, comes from upstream package
Patch0:         gtk+-2.24.14-INITGUID.patch
                # BXC10144 - Solution pad continues scrolling to follow mouse after aborted drag
                # https://bugzilla.xamarin.com/show_bug.cgi?id=10144
Patch1:	        0001-aborted-drag-should-leave.patch
                # BXC10790 - tabs stop responding to clicks
                # https://bugzilla.xamarin.com/show_bug.cgi?id=10790
Patch2:         0002-recreate-cairo-surfaces-if-needed.patch
                # BXC11281 - Drag & Drop not working in 'auto-hide' pads
                # https://bugzilla.xamarin.com/show_bug.cgi?id=11281
Patch3:		    0003-fix-dnd-in-autohide-pads.patch
                # BXC4205 - Incompatible with United States-International keyboard layout
                # https://bugzilla.xamarin.com/show_bug.cgi?id=4205
Patch4:         0004-choose-ime-based-on-locale.patch
                # BXC1474 - IME candidate window on Windows has offset position
                # https://bugzilla.xamarin.com/show_bug.cgi?id=1474
Patch5:         0005-fix-ime-candidate-location.patch
                # BXC11597 - Xamarin studio randomly crash when working via rdesktop
                # https://bugzilla.xamarin.com/show_bug.cgi?id=11597
Patch6:         0006-release-allocated-16bpp-objects.patch
                # BXC9744 - GTK+ has rendering issues on high-DPI Windows setups
                # https://bugzilla.xamarin.com/show_bug.cgi?id=9744
Patch7:         0007-set-gdkscreen-resolution.patch
                # BXC10644 - [gtk] Xamarin Studio stuck on top
                # https://bugzilla.xamarin.com/show_bug.cgi?id=10644
Patch8:         0008-never-restack-below-temp.patch
                # https://bugzilla.xamarin.com/show_bug.cgi?id=4205
Patch9:         0009-gtkimcontextime-deadkeys.patch
                # https://bugzilla.xamarin.com/show_bug.cgi?id=15893
Patch10:        0010-disable-combobox-scrolling.patch
Patch11:        0011-remove-window-pos-changing-stacking.patch
Patch12:        0012-dont-override-icon-size-in-mswindows-theme.patch
Patch13:        0013-treeview-combobox-dont-appear-as-list.patch
Patch14:        0016-retina-icons.patch
Patch15:        0017-win32-scale-factor.patch
Patch16:        0018-win32-dpi-awareness.patch
Patch17:        0019-fix-win32-exports.patch
Patch18:        0020-scaled-image-win32.patch
Patch19:        0021-round-scale-up-to-2-0.patch
Patch20:        0022-combobox-rendering.patch
Patch21:        generate-grab-broken.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildArch:      noarch
#!BuildIgnore: post-build-checks

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  mingw32-atk-devel >= 1.29.3
BuildRequires:  mingw32-cairo-devel
BuildRequires:  mingw32-cross-binutils
BuildRequires:  mingw32-cross-gcc
BuildRequires:  mingw32-cross-pkg-config
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gdk-pixbuf-devel
BuildRequires:  mingw32-glib2-devel
BuildRequires:  mingw32-libintl-devel
BuildRequires:  mingw32-libjasper-devel
BuildRequires:  mingw32-pango-devel >= 1.20
BuildRequires:  mingw32-win_iconv-devel
BuildRequires:  xz
# Native version for glib-genmarshal
BuildRequires:  glib2-devel
# Native version for gtk-update-icon-cache
%if 0%{?suse_version} >= 1140
BuildRequires:  gtk2-tools
%else
BuildRequires:  gtk2
%endif
# Native version for gdk-pixbuf-csource
%if 0%{?suse_version} >= 1140
BuildRequires:  gdk-pixbuf-devel
%else
BuildRequires:  gtk2-devel
%endif
Requires:       %{name}-lang = %{version}

%description
GTK+ is a highly usable, feature rich toolkit for creating graphical user interfaces which boasts cross platform
compatibility and an easy to use API.

GTK+ was initially developed for and used by the GIMP, the GNU Image Manipulation Program. It is called the "The GIMP
ToolKit" so that the origins of the project are remembered. Today it is more commonly known as GTK+ for short and is
used by a large number of applications including the GNU project's GNOME desktop.


%package tools
Summary:        GTK+2 GUI library (tools)
Group:          System/Libraries

%description tools
GTK+ is a highly usable, feature rich toolkit for creating graphical user interfaces which boasts cross platform
compatibility and an easy to use API.


%package devel
Summary:        Development environment for the GTK+2 GUI library
Group:          Development/Libraries

%description devel
This package contains all necessary include files, libraries, configuration files and development tools needed to
compile and link applications using the GTK+ library.

In addition, it contains a large set of demo applications in source code and manual pages for the provided GTK+
development tools.


%{_mingw32_debug_package}

%lang_package

%prep
%setup -q -n gtk+-%{version}

%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1

%build
autoreconf -f -i
# Need to run the correct version of glib-mkenums.
export PATH="%{_mingw32_bindir}:$PATH"

echo "lt_cv_deplibs_check_method='pass_all'" >>%{_mingw32_cache}

#cups is pointless for win32
%{_mingw32_configure} \
	--disable-cups --with-gdktarget=win32 \
	--with-included-immodules=yes
rm -f gtk/gtk.def gdk/gdk.def
make %{?_smp_mflags} || make

%install
make DESTDIR=$RPM_BUILD_ROOT install

chmod -x $RPM_BUILD_ROOT%{_mingw32_libdir}/*.def
rm $RPM_BUILD_ROOT%{_mingw32_bindir}/*.manifest

(echo 'gtk-theme-name = "MS-Windows"'
echo 'gtk-fallback-icon-theme = "Tango"') >$RPM_BUILD_ROOT%{_mingw32_sysconfdir}/gtk-2.0/gtkrc

%find_lang gtk20
%find_lang gtk20-properties gtk20.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_mingw32_datadir}/themes/*
%{_mingw32_bindir}/libgailutil-18.dll
%{_mingw32_bindir}/libgdk-win32-2.0-0.dll
%{_mingw32_bindir}/libgtk-win32-2.0-0.dll
%{_mingw32_libdir}/gtk-2.0/2.10.0/engines/*.dll
%{_mingw32_libdir}/gtk-2.0/modules/*.dll
%{_mingw32_sysconfdir}/gtk-2.0/

%files tools
%defattr(-,root,root)
%{_mingw32_bindir}/gtk-query-immodules-2.0.exe
%{_mingw32_bindir}/gtk-update-icon-cache.exe

%files lang -f gtk20.lang
%defattr(-,root,root)

%files devel
%defattr(-,root,root)
%{_mingw32_bindir}/gtk-builder-convert
%exclude %{_mingw32_bindir}/gtk-demo.exe
%{_mingw32_libdir}/libgailutil.dll.a
%{_mingw32_libdir}/libgdk-win32-2.0.dll.a
%{_mingw32_libdir}/libgtk-win32-2.0.dll.a
%{_mingw32_libdir}/gdk-win32-2.0.def
%{_mingw32_libdir}/gtk-win32-2.0.def
%{_mingw32_libdir}/gailutil.def
%{_mingw32_libdir}/pkgconfig/gail.pc
%{_mingw32_libdir}/pkgconfig/gdk-2.0.pc
%{_mingw32_libdir}/pkgconfig/gdk-win32-2.0.pc
%{_mingw32_libdir}/pkgconfig/gtk+-2.0.pc
%{_mingw32_libdir}/pkgconfig/gtk+-win32-2.0.pc
%exclude %{_mingw32_libdir}/gtk-2.0/2.10.0/engines/*.dll.a
%exclude %{_mingw32_libdir}/gtk-2.0/modules/*.dll.a
%{_mingw32_includedir}/gtk-2.0/
%{_mingw32_libdir}/gtk-2.0/include/
%{_mingw32_includedir}/gail-1.0/
%{_mingw32_datadir}/aclocal/gtk-2.0.m4
%{_mingw32_datadir}/gtk-2.0/
%{_mingw32_datadir}/gtk-doc/html/gail-libgail-util
%{_mingw32_datadir}/gtk-doc/html/gdk2
%{_mingw32_datadir}/gtk-doc/html/gtk2

%changelog
