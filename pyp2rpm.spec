Name:		pyp2rpm
Version:	3.3.10
Release:	1
Group:		Development/Python
Summary:	Convert Python packages to RPM SPECFILES
License:	MIT
URL:		https://github.com/fedora-python/pyp2rpm
Source0:	https://files.pythonhosted.org/packages/source/p/pyp2rpm/pyp2rpm-%{version}.tar.gz
Patch0:		add-openmandriva-spec-template.patch
Patch1:		add-openmandriva.patch
BuildArch:	noarch
 
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(click)
BuildRequires:	python%{pyver}dist(flexmock) >= 0.9.3
BuildRequires:	python%{pyver}dist(jinja2)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
#BuildRequires:  python%{pyver}dist(virtualenv-api)
BuildRequires:  python%{pyver}dist(pytest-runner)
#BuildRequires:  python%{pyver}dist(scripttest)
#BuildRequires:  vex

%description
Convert Python packages to RPM SPECFILES. 
Packages can be downloaded from PyPI and the product 
is in line with Fedora Packaging Guidelines or Mageia Python Policy

%files
%license LICENSE
%{_bindir}/pyp2rpm
%{py_puresitedir}/pyp2rpm
%{py_puresitedir}/pyp2rpm-%{version}-py%{python_version}.*-info
%{_mandir}/man1/pyp2rpm.1*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n pyp2rpm-%{version}

# Remove bundled egg-info
rm -rf pyp2rpm.egg-info

%build
%py_build

%install
%py_install

# man
mkdir -p %{buildroot}%{_mandir}/man1/
zstd -i pyp2rpm.1 -o %{buildroot}/%{_mandir}/man1/pyp2rpm.1.zst

