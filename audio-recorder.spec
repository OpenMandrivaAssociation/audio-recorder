%define gstapi 1.0
%define ubuntuversion jammy

Summary:	Audio recorder for the GNOME
Name:		audio-recorder
Version:	3.3.4
Release:	1
License:	GPLv3+
Group:		Sound
Url:		https://launchpad.net/audio-recorder
#Source0:	https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}_%{version}.tar.xz
Source0:  %{url}/+archive/ubuntu/ppa/+sourcefiles/audio-recorder/%{version}~%{ubuntuversion}/audio-recorder_%{version}~%{ubuntuversion}.tar.gz
BuildRequires:	intltool
#BuildRequires:  gstpbutils1.0_0
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(dconf)
BuildRequires:	pkgconfig(glib-2.0)
#BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:  pkgconfig(appindicator3-0.1)
Requires:	gstreamer%{gstapi}-plugins-bad
Requires:	gstreamer%{gstapi}-plugins-base
Requires:	gstreamer%{gstapi}-plugins-good
Recommends:	gstreamer%{gstapi}-plugins-ugly

%description
Audio-recorder allows you to record your favourite music or audio to
a file. It can record audio from your system's soundcard,
microphones, browsers, webcams & more. Put simply: if it plays out of
your loudspeakers you can record it.

%files -f %{name}.lang
%doc ChangeLog README COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
#{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*
%{_datadir}/pixmaps/%{name}/
%{_datadir}/glib-2.0/schemas/org.gnome.audio-recorder.gschema.xml
%{_mandir}/man1/%{name}.1*

#----------------------------------------------------------------------------

%prep
%autosetup -n trunk -p1

%build
%configure
%make_build

%install
%make_install

%find_lang %{name}

