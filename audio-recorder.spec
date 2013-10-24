%define gstapi 1.0

Summary:	Audio recorder for the GNOME
Name:		audio-recorder
Version:	1.3
Release:	1
License:	GPLv3+
Group:		Sound
Url:		https://launchpad.net/audio-recorder
Source0:	https://launchpad.net/audio-recorder/trunk/version%{version}-1/+download/%{name}-%{version}-1.tar.gz
Patch0:		audio-recorder-correct-desktop-menu.patch
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(dconf)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libpulse)
Requires:	gstreamer%{gstapi}-plugins-bad
Requires:	gstreamer%{gstapi}-plugins-base
Requires:	gstreamer%{gstapi}-plugins-good
Requires:	gstreamer%{gstapi}-plugins-ugly

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
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/pixmaps/%{name}/
%{_datadir}/glib-2.0/schemas/org.gnome.audio-recorder.gschema.xml

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}
