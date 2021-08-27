Name: qmf-qt5
Summary:    Qt Messaging Framework (QMF) Qt5
Version:    4.0.4+git127
Release:    1
License:    (LGPLv2 or LGPLv3) with exception or Qt Commercial
URL:        https://code.qt.io/qt-labs/messagingframework.git
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
BuildRequires:  pkgconfig(keepalive)
BuildRequires:  pkgconfig(qt5-boostable)
#Needed for qhelpgenerator
BuildRequires:  qt5-qttools-qthelp-devel
BuildRequires:  qt5-plugin-platform-minimal
BuildRequires:  qt5-plugin-sqldriver-sqlite
BuildRequires:  fdupes
BuildRequires:  gpgme-devel
BuildRequires:  systemd
Requires:       buteo-syncfw-qt5 >= 0.7.16 

Patch1:  0001-Introduce-acceptUntrustedCertificates-configuration.patch
Patch2:  0002-fix-tests-installation-path.patch
Patch3:  0003-Accounts-qt-integration.patch
Patch4:  0004-Start-messageserver-on-system-startup-in-case-there-.patch
Patch5:  0005-Add-keepalive-timer-to-IMAP-IDLE-service.patch
Patch6:  0006-Use-Qt5-booster-to-save-memory.patch
Patch7:  0007-Introduce-QMailAccount-HasPersistentConnection-statu.patch
Patch8:  0008-Introduce-discovery-of-authentication-from-the-anoun.patch
Patch9:  0009-Handle-SMTP-response-504.patch
Patch10: 0010-Recreate-SSO-identity-for-smtp-in-case-of-failure.patch
Patch11: 0011-Listen-to-sync-schedule-changes-from-buteo-sync-fram.patch
Patch12: 0012-Do-AUTHENTICATE-PLAIN-in-two-stages.patch
Patch13: 0013-Prevent-push-enabled-status-to-go-out-of-sync.patch
Patch14: 0014-Add-signature-settings-in-account.patch
Patch15: 0015-Use-EightBit-encoding-instead-of-Base64-for-text-typ.patch
Patch16: 0016-Set-qmf-accountscheck-to-be-run-by-the-booster.patch
Patch17: 0017-Retrieve-message-lists-based-on-the-folder-sync-poli.patch
Patch18: 0018-Apply-folder-policy-to-always-on-connection.patch
Patch19: 0019-Allow-a-service-provided-folder-to-be-set-as-the-sta.patch
Patch20: 0020-Add-QMailMessage-CalendarCancellation-flag.patch
Patch21: 0021-Use-a-queued-connection-to-handle-accountsUpdated-si.patch
Patch22: 0022-Store-socket-in-RuntimeLocation.patch
Patch23: 0023-Handle-encoded-word-s-containing-partial-characters.patch
Patch24: 0024-Revert-Fix-bundled-zlib-detection.patch
Patch25: 0025-Revert-Use-QRandomGenerator-instead-of-qrand.patch
Patch26: 0026-Revert-Use-range-constructors-for-lists-and-sets.patch
Patch27: 0027-Revert-Adjust-to-Qt6-QMetaType-API-changes.patch
Patch28: 0028-Revert-Replace-deprecated-QString-SplitBehavior.patch
Patch29: 0029-Revert-Fix-disappearance-of-QDateTime-QDate.patch
Patch30: 0030-Revert-core5compat-addition.patch
Patch31: 0031-Adjust-qmflist-for-missing-bits-in-5.6.patch
Patch32: 0032-Revert-loadRelax.patch
Patch33: 0033-Revert-Set-PLUGIN_CLASS_NAME-in-plugin-.pro-files.patch
Patch34: 0034-Revert-Bump-version-to-6.0.0-since-we-build-against-.patch
Patch35: 0035-Fix-bug-when-detecting-HEADER-BODY-substrings.patch

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
    DEFINES+=QMF_ENABLE_LOGGING \
    DEFINES+=MESSAGESERVER_PLUGINS \
    DEFINES+=QMF_NO_MESSAGE_SERVICE_EDITOR \
    DEFINES+=QMF_NO_WIDGETS \
    DEFINES+=USE_ACCOUNTS_QT \
    DEFINES+=USE_KEEPALIVE \
    DEFINES+=USE_HTML_PARSER \
    CONFIG+=syslog

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
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
%defattr(-,root,root,-)
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
%defattr(-,root,root,-)
%{_bindir}/messageserver5
%{_bindir}/qmf-accountscheck
%{_datadir}/mapplauncherd/privileges.d/*
%{_libdir}/libQmfMessageServer.so.*
%{_libdir}/qt5/plugins/messageservices
%{_userunitdir}/*.service
%{_userunitdir}/user-session.target.wants/*.service

%files -n libqmfclient1-qt5
%defattr(-,root,root,-)
%license LICENSE.LGPLv* LGPL_EXCEPTION.txt
%{_libdir}/libQmfClient.so.*
%{_libdir}/qt5/plugins/contentmanagers
%{_libdir}/qt5/plugins/ssoauth

%files -n libqmfclient1-qt5-cryptoplugins
%{_libdir}/qt5/plugins/crypto

%if 0
%files tests
%defattr(-,root,root,-)
%{_datadir}/accounts/*
/opt/tests/qmf-qt5
%else
%exclude %{_datadir}/accounts/*
%endif
