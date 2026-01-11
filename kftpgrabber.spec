%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg kftpgrabber
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Epoch:			%{tde_epoch}
Version:        0.8.1
Release:		%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:        A FTP client for TDE
Group:          Applications/Internet
URL:            http://www.kftp.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/internet/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
KFTPgrabber is a graphical FTP client for the Trinity Desktop Environment. It
implements many features required for usable FTP interaction.

Feature list:
- Multiple simultaneous FTP sessions in separate tabs
- A tree-oriented transfer queue
- TLS/SSL support for the control connection and the data channel
- X509 certificate support for authentication
- FXP site-to-site transfer support
- One-time password (OTP) support using S/KEY, MD5, RMD160 or SHA1
- Site bookmarks with many options configurable per-site
- Distributed FTP daemon support (implementing the PRET command)
- Can use Zeroconf for local site discovery
- Bookmark import plugins from other FTP clients
- Support for the SFTP protocol
- A nice traffic graph
- Ability to limit upload and download speed
- Priority and skip lists
- Integrated SFV checksum verifier
- Direct viewing/editing of remote files
- Advanced default "on file exists" action configuration
- Filter displayed files/directories as you type


%package devel
Summary:  	Development files for %{name}
Group: 		Development/Libraries
Requires: 	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}


%conf -p
unset QTDIR QTINC QTDIR
export PATH="%{tde_prefix}/bin:${PATH}"


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.md ChangeLog
%{tde_prefix}/bin/kftpgrabber
%{tde_prefix}/%{_lib}/libkftpinterfaces.so.0
%{tde_prefix}/%{_lib}/libkftpinterfaces.so.0.0.0
%{tde_prefix}/%{_lib}/trinity/kftpimportplugin_filezilla3.la
%{tde_prefix}/%{_lib}/trinity/kftpimportplugin_filezilla3.so
%{tde_prefix}/%{_lib}/trinity/kftpimportplugin_gftp.la
%{tde_prefix}/%{_lib}/trinity/kftpimportplugin_gftp.so
%{tde_prefix}/%{_lib}/trinity/kftpimportplugin_kftp.la
%{tde_prefix}/%{_lib}/trinity/kftpimportplugin_kftp.so
%{tde_prefix}/%{_lib}/trinity/kftpimportplugin_ncftp.la
%{tde_prefix}/%{_lib}/trinity/kftpimportplugin_ncftp.so
%{tde_prefix}/share/applications/tde/kftpgrabber.desktop
%{tde_prefix}/share/apps/kftpgrabber/
%{tde_prefix}/share/config.kcfg/kftpgrabber.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kftpgrabber.png
%{tde_prefix}/share/services/kftpimportplugin_filezilla3.desktop
%{tde_prefix}/share/services/kftpimportplugin_gftp.desktop
%{tde_prefix}/share/services/kftpimportplugin_kftp.desktop
%{tde_prefix}/share/services/kftpimportplugin_ncftp.desktop
%{tde_prefix}/share/servicetypes/kftpbookmarkimportplugin.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kftpgrabber/
%{tde_prefix}/share/man/man1/kftpgrabber.1*


%files devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/kftpgrabber/
%{tde_prefix}/%{_lib}/libkftpinterfaces.la
%{tde_prefix}/%{_lib}/libkftpinterfaces.so

