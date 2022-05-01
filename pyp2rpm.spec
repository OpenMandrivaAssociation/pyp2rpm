%global module pyp2rpm

Name:		pyp2rpm
Version:	3.3.8
Release:	1
Group:		Development/Python
Summary:	Convert Python packages to RPM SPECFILES
License:	MIT
URL:		https://github.com/fedora-python/pyp2rpm
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
Patch0:		add-openmandriva-spec-template.patch
Patch1:		add-openmandriva.patch
BuildArch:	noarch
 
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
BuildRequires:  python3dist(click)
BuildRequires:	python3dist(flexmock) >= 0.9.3
BuildRequires:	python3dist(jinja2)
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(wheel)
#BuildRequires:  python3dist(virtualenv-api)
BuildRequires:  python3dist(pytest-runner)
#BuildRequires:  python3dist(scripttest)
#BuildRequires:  vex

%description
Convert Python packages to RPM SPECFILES. 
Packages can be downloaded from PyPI and the product 
is in line with Fedora Packaging Guidelines or Mageia Python Policy

%files
%license LICENSE
%{_bindir}/pyp2rpm
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}-py%{python_version}.egg-info
%{_mandir}/man1/pyp2rpm.1*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{module}-%{version}

# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py_build

%install
%py_install

# man
mkdir -p %{buildroot}%{_mandir}/man1/
zstd -i pyp2rpm.1 -o %{buildroot}/%{_mandir}/man1/pyp2rpm.1.zst

