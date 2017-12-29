Name: qmf-qt5
Summary:    Qt Messaging Framework (QMF) Qt5
Version:    4.0.4+git63
Release:    1
Group:      System/Libraries
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.gitorious.org/qt-labs/messagingframework
Source0:    %{name}-%{version}.tar.bz2
Requires:   systemd-user-session-targets
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires: 	pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(accounts-qt5) >= 1.13
BuildRequires:  pkgconfig(libsignon-qt5)
BuildRequires:  pkgconfig(keepalive)
BuildRequires:  pkgconfig(qt5-boostable)
#Needed for qhelpgenerator
BuildRequires:  qt5-qttools-qthelp-devel
BuildRequires:  qt5-plugin-platform-minimal
BuildRequires:  qt5-plugin-sqldriver-sqlite
BuildRequires:  fdupes
Requires:       buteo-syncfw-qt5 >= 0.7.16 

%description
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.


%package devel
Summary:    Qt Messaging Framework (QMF) Qt5 - development files
Group:      Development/Libraries
Requires:   libqmfmessageserver1-qt5 = %{version}
Requires:   libqmfclient1-qt5 = %{version}

%description devel
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

This package contains the development files needed to build Qt applications
using Qt Messaging Framework libraries.


%package -n libqmfmessageserver1-qt5
Summary:    Qt Messaging Framework (QMF) message server support library
Group:      System/Libraries
Requires:   qt5-qtsql
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n libqmfmessageserver1-qt5
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

The MessageServer application is a daemon, designed to run continuously while
providing services to client applications. It provides messaging transport
functionality, communicating with external servers on behalf of Messaging
Framework client applications. New types of messaging (such as Instant
Messages or video messages) can be handled by the server application without
modification to existing client applications.

This package contains:
 - the message server support library. It provides assistance in developing GUI
   clients that access messaging data.
 - a server application supporting multiple messaging transport mechanisms.


%package -n libqmfclient1-qt5
Summary:    Qt Messaging Framework (QMF) client library
Group:      System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n libqmfclient1-qt5
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

The Client library provides classes giving access to all messages stored on
the device, via a uniform interface. It simplifies the task of creating
messaging client applications, and permits other Messaging Framework
applications to interact with messaging data where appropriate. New types of
messages can be supported by the library without modification to existing
client applications.

This package contains a library for developing applications that work with
messages.


%package tests
Summary:    Qt Messaging Framework (QMF) tests
Group:      System/X11

%description tests
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

This package contains the tests for Qt Messaging Framework (QMF).


%package doc
Summary:    Qt Messaging Framework (QMF) - documentation
Group:      Documentation
BuildArch:    noarch

%description doc
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

This package contains the documentation for Qt Messaging Framework (QMF).

%prep
%setup -q -n %{name}-%{version}/qmf

%build

%qmake5  \
    QMF_INSTALL_ROOT=%{_prefix} \
    DEFINES+=QMF_ENABLE_LOGGING \
    DEFINES+=MESSAGESERVER_PLUGINS \
    DEFINES+=QMF_NO_MESSAGE_SERVICE_EDITOR \
    DEFINES+=USE_KEEPALIVE \
    DEFINES+=USE_HTML_PARSER \
    CONFIG+=syslog

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install
UNIT_DIR=%{buildroot}%{_libdir}/systemd/user/user-session.target.wants
mkdir -p "$UNIT_DIR"
ln -sf ../messageserver5.service "$UNIT_DIR/messageserver5.service"
ln -sf ../messageserver5-accounts-check.service "$UNIT_DIR/messageserver5-accounts-check.service"

%fdupes  %{buildroot}/%{_includedir}

%post -n libqmfmessageserver1-qt5 -p /sbin/ldconfig

%postun -n libqmfmessageserver1-qt5 -p /sbin/ldconfig

%post -n libqmfclient1-qt5 -p /sbin/ldconfig

%postun -n libqmfclient1-qt5 -p /sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%{_includedir}/qmfmessageserver5/qmail*.h
%{_includedir}/qmfclient5/qloggers.h
%{_includedir}/qmfclient5/qlogsystem.h
%{_includedir}/qmfclient5/qmail*.h
%{_includedir}/qmfclient5/qprivateimplementation.h
%{_includedir}/qmfclient5/qprivateimplementationdef.h
%{_includedir}/qmfclient5/sso*.h
%{_libdir}/libqmfmessageserver5.prl
%{_libdir}/libqmfmessageserver5.so
%{_libdir}/libqmfclient5.prl
%{_libdir}/libqmfclient5.so
%{_libdir}/pkgconfig/qmfmessageserver5.pc
%{_libdir}/pkgconfig/qmfclient5.pc

%files -n libqmfmessageserver1-qt5
%defattr(-,root,root,-)
%{_bindir}/messageserver5
%{_bindir}/qmf-accountscheck
%{_libdir}/libqmfmessageserver5.so.*
%{_libdir}/qmf/plugins5/messageservices/libimap.so
%{_libdir}/qmf/plugins5/messageservices/libpop.so
%{_libdir}/qmf/plugins5/messageservices/libqmfsettings.so
%{_libdir}/qmf/plugins5/messageservices/libsmtp.so
%{_libdir}/systemd/user/messageserver5.service
%{_libdir}/systemd/user/messageserver5-accounts-check.service
%{_libdir}/systemd/user/user-session.target.wants/messageserver5.service
%{_libdir}/systemd/user/user-session.target.wants/messageserver5-accounts-check.service

%files -n libqmfclient1-qt5
%defattr(-,root,root,-)
%{_libdir}/libqmfclient5.so.*
%{_libdir}/qmf/plugins5/contentmanagers/libqmfstoragemanager.so
%{_libdir}/qmf/plugins5/ssoauth/libpasswordplugin.so

%files tests
%defattr(-,root,root,-)
%{_datadir}/accounts/*
/opt/tests/qmf-qt5/*

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/qmf-qt5/qch/qmf.qch
