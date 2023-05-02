Summary:	A simple GUI for managing Conky config files
Name:		conky-manager2
Version:	2.7
Release:	1
Group:		Monitoring
License:	GPLv3+
URL:		https://github.com/zcot/conky-manager2
Source0:	https://github.com/zcot/conky-manager2/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	meson
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	vala

Requires:	conky
Requires:	lm_sensors
Requires:	hddtemp
Requires:	7zip

%rename conky-manager
Obsoletes:	conky-manager < %{version}

%description
A simple GUI for managing Conky config files. Options for changing themes and
running Conky at startup.

%files -f %name.lang
%license COPYING
%doc README.md AUTHORS TODO
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

# icons
for d in 16 32 48 64 72 128 256 512
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	convert -background none  -scale ${d}x${d} src/share/%{name}/images/%{name}.png \
			%{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
convert -background none  -scale ${d}x${d} src/share/%{name}/images/%{name}.png \
		%{buildroot}%{_datadir}/pixmaps/%{name}.xpm

# locales
%find_lang %name --all-name

#rm -f %{buildroot}/%{_bindir}/%{name}2-uninstall
