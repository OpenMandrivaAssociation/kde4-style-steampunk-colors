Summary:	"SteampunK Powered Linux" colors for KDE and QtCurve
Name:		kde4-style-steampunk-colors
Version:	3.0
Release:	2
License:	Creative Commons Attribution-ShareAlike
Group:		Graphical desktop/KDE
# Also http://kde-look.org/content/show.php?content=148276
# and http://kde-look.org/content/show.php/SteampunK+Light+Color+Scheme?content=155868
Url:		https://kde-look.org/content/show.php?content=148277
# Repack from all sources:
Source:		SteampunK_Colors.tar.gz
Requires:	kdebase4-workspace >= 2:4.10
BuildRequires:	kde4-macros
BuildArch:	noarch

%description
This package contains the "SteampunK Powered Linux" colors for KDE and QtCurve.

%files
%{_kde_appsdir}/color-schemes/*.colors
%{_kde_appsdir}/QtCurve/*.qtcurve

#----------------------------------------------------------------------------

%prep
%setup -q -c
find . -type f | xargs chmod 0644

%build
# nothing

%install
mkdir -p %{buildroot}%{_kde_appsdir}/color-schemes/
mkdir -p %{buildroot}%{_kde_appsdir}/QtCurve/

cp SteampunK/{SteampunK,SteampunKLight}.colors %{buildroot}%{_kde_appsdir}/color-schemes/
cp SteampunK/{SteampunK,SteampunkLight}.qtcurve %{buildroot}%{_kde_appsdir}/QtCurve/

