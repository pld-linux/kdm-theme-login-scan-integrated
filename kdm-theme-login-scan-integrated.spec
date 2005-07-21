
%define		_theme		login-scan-integrated

Summary:	login-scan 'integrated' KDM theme
Summary(pl):	Motyw KDM login-scan 'integrated'
Name:		kdm-theme-%{_theme}
Version:	01
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://www.kde-look.org/content/files/26718-%{_theme}.tar.gz
# Source0-md5:	accd6932cc8f6a6bb0abe0ae2daa73e9
URL:		http://www.kde-look.org/content/show.php?content=26718
Requires:	kdebase-desktop >= 9:3.2.0
Requires:	kdmtheme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
login-scan 'integrated' KDM Theme.

%description -l pl
Motyw KDM login-scan 'integrated'.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_theme}

install %{_theme}/*.{desktop,jpg,png,xml} $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_theme}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kdm/themes/%{_theme}
