Name: qmf-qt5
Summary:    Qt Messaging Framework (QMF) Qt5
Version:    4.0.4+git166
Release:    1
License:    (LGPLv2 or LGPLv3) with exception or Qt Commercial
URL:        https://github.com/sailfishos/messagingframework
Source0:    %{name}-%{version}.tar.bz2
Source1:    %{name}.privileges
Source2:    qmf-accountscheck.privileges
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
BuildRequires:  pkgconfig(signon-oauth2plugin)
BuildRequires:  pkgconfig(libsailfishkeyprovider)
BuildRequires:  pkgconfig(keepalive)
BuildRequires:  pkgconfig(qt5-boostable)
BuildRequires:  pkgconfig(systemd)
#Needed for qhelpgenerator
BuildRequires:  qt5-qttools-qthelp-devel
BuildRequires:  qt5-plugin-platform-minimal
BuildRequires:  qt5-plugin-sqldriver-sqlite
BuildRequires:  fdupes
BuildRequires:  gpgme-devel
Requires:       buteo-syncfw-qt5 >= 0.7.16 

# i=1; for j in 00*patch; do printf "Patch%04d: %s\n" $i $j; i=$((i+1));done
Patch0001: 0001-fix-tests-installation-path.patch
Patch0002: 0002-Accounts-qt-integration.patch
Patch0003: 0003-Start-messageserver-on-system-startup-in-case-there-.patch
Patch0004: 0004-Add-keepalive-timer-to-IMAP-IDLE-service.patch
Patch0005: 0005-Use-Qt5-booster-to-save-memory.patch
Patch0006: 0006-Listen-to-sync-schedule-changes-from-buteo-sync-fram.patch
Patch0007: 0007-Use-EightBit-encoding-instead-of-Base64-for-text-typ.patch
Patch0008: 0008-Retrieve-message-lists-based-on-the-folder-sync-poli.patch
Patch0009: 0009-Apply-folder-policy-to-always-on-connection.patch
Patch0010: 0010-Allow-a-service-provided-folder-to-be-set-as-the-sta.patch
Patch0011: 0011-Adjust-for-Qt-5.6.patch
Patch0012: 0012-Revert-Fix-bundled-zlib-detection.patch
Patch0013: 0013-Revert-Use-QRandomGenerator-instead-of-qrand.patch
Patch0014: 0014-Revert-Use-range-constructors-for-lists-and-sets.patch
Patch0015: 0015-Revert-Adjust-to-Qt6-QMetaType-API-changes.patch
Patch0016: 0016-Revert-Replace-deprecated-QString-SplitBehavior.patch
Patch0017: 0017-Revert-core5compat-addition.patch
Patch0018: 0018-Adjust-qmflist-for-missing-bits-in-5.6.patch
Patch0019: 0019-Revert-loadRelax.patch
Patch0020: 0020-Revert-Fix-disappearance-of-QDateTime-QDate.patch
Patch0021: 0021-Revert-Set-PLUGIN_CLASS_NAME-in-plugin-.pro-files.patch
Patch0022: 0022-Revert-Bump-version-to-6.0.0-since-we-build-against-.patch
Patch0023: 0023-Fallback-to-sso-credential-plugin.patch
Patch0024: 0024-Revert-private-header-paths.patch


%description
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.


%package devel
Summary:    Qt Messaging Framework (QMF) Qt5 - development files
Requires:   libqmfmessageserver1-qt5 = %{version}
Requires:   libqmfclient1-qt5 = %{version}
# depending packages get linkage to following which doesn't work without .so files
Requires:   pkgconfig(accounts-qt5)
Requires:   pkgconfig(libsignon-qt5)
# FIXME: these shouldn't really be needed by depending packages, but upstream
# currently forces explicit linkage on mostly everything used on its own build
Requires:   pkgconfig(Qt5Core)
Requires:   pkgconfig(Qt5Gui)
Requires:   pkgconfig(Qt5Sql)
Requires:   pkgconfig(Qt5Network)


%description devel
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

This package contains the development files needed to build Qt applications
using Qt Messaging Framework libraries.


%package -n libqmfmessageserver1-qt5
Summary:    Qt Messaging Framework (QMF) message server support library
Requires:   qt5-qtsql
Requires:   qt5-plugin-platform-minimal
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   qmf-oauth2-plugin
Obsoletes:  qmf-oauth2-plugin <= 0.1.0

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

%package -n libqmfclient1-qt5-cryptoplugins
Summary:    QMF crypto plugins
Requires:   libqmfclient1-qt5 = %{version}
Requires:   dirmngr

%description -n libqmfclient1-qt5-cryptoplugins
This package contains the cryptographic plugins for email signing


# TODO: upstream stopped installing tests. get them back.
%if 0
%package tests
Summary:    Qt Messaging Framework (QMF) tests

%description tests
The Qt Messaging Framework, QMF, consists of a C++ library and daemon server
process that can be used to build email clients, and more generally software
that interacts with email and mail servers.

This package contains the tests for Qt Messaging Framework (QMF).
%endif


%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build

# syncqt.pl doesn't generate headers if build is not detected to be git_build
touch .git

%qmake5 \
    QT_BUILD_PARTS+=tests \
    QMF_INSTALL_ROOT=%{_prefix} \
    DEFINES+=MESSAGESERVER_PLUGINS \
    DEFINES+=QMF_NO_MESSAGE_SERVICE_EDITOR \
    DEFINES+=QMF_NO_WIDGETS \
    DEFINES+=USE_ACCOUNTS_QT \
    DEFINES+=USE_KEEPALIVE \
    DEFINES+=USE_HTML_PARSER

%make_build

%install
%qmake5_install
UNIT_DIR=%{buildroot}%{_userunitdir}/user-session.target.wants
mkdir -p "$UNIT_DIR"
ln -sf ../messageserver5.service "$UNIT_DIR/messageserver5.service"
ln -sf ../messageserver5-accounts-check.service "$UNIT_DIR/messageserver5-accounts-check.service"

mkdir -p %{buildroot}%{_datadir}/mapplauncherd/privileges.d
install -m 644 -p %{SOURCE1} %{buildroot}%{_datadir}/mapplauncherd/privileges.d
install -m 644 -p %{SOURCE2} %{buildroot}%{_datadir}/mapplauncherd/privileges.d

%fdupes  %{buildroot}/%{_includedir}

%post -n libqmfmessageserver1-qt5 -p /sbin/ldconfig

%postun -n libqmfmessageserver1-qt5 -p /sbin/ldconfig

%post -n libqmfclient1-qt5 -p /sbin/ldconfig

%postun -n libqmfclient1-qt5 -p /sbin/ldconfig

%files devel
%{_includedir}/qt5/QmfClient
%{_includedir}/qt5/QmfMessageServer
%exclude %{_libdir}/cmake/Qt5QmfClient/Qt5QmfClient_.cmake
%exclude %{_libdir}/cmake/Qt5QmfMessageServer/Qt5QmfMessageServer_.cmake
%{_libdir}/libQmfMessageServer.prl
%{_libdir}/libQmfMessageServer.so
%exclude %{_libdir}/libQmfMessageServer.la
%{_libdir}/libQmfClient.prl
%{_libdir}/libQmfClient.so
%exclude %{_libdir}/libQmfClient.la
%{_libdir}/pkgconfig/QmfMessageServer.pc
%{_libdir}/pkgconfig/QmfClient.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_qmfclient.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_qmfclient_private.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_qmfmessageserver.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_qmfmessageserver_private.pri

%files -n libqmfmessageserver1-qt5
%{_bindir}/messageserver5
%{_bindir}/qmf-accountscheck
%{_datadir}/mapplauncherd/privileges.d/*
%{_libdir}/libQmfMessageServer.so.*
%{_libdir}/qt5/plugins/messageservices
%{_libdir}/qt5/plugins/messagecredentials
%{_userunitdir}/*.service
%{_userunitdir}/user-session.target.wants/*.service

%files -n libqmfclient1-qt5
%license LICENSE.LGPLv* LGPL_EXCEPTION.txt
%{_libdir}/libQmfClient.so.*
%{_libdir}/qt5/plugins/contentmanagers

%files -n libqmfclient1-qt5-cryptoplugins
%{_libdir}/qt5/plugins/crypto

%if 0
%files tests
%{_datadir}/accounts/*
/opt/tests/qmf-qt5
%else
%exclude %{_datadir}/accounts/*
%endif
