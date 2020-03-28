# Created by pyp2rpm-2.0.0
%global pypi_name pyp2rpm
%global with_python2 0
%define version 3.3.3

Name:           python-pyp2rpm
Version:        %{version}
Release:        1
Group:          Development/Python
Summary:        Convert Python packages to RPM SPECFILES

License:        MIT
URL:            https://github.com/fedora-python/pyp2rpm
Source0:        https://pypi.python.org/packages/89/83/efcc943c2aa19cb348433b08dcd7a055e58bb4db224d41769b2a33968949/pyp2rpm-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-flexmock >= 0.9.3
BuildRequires:  python-pytest
 
%if %{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-flexmock >= 0.9.3
BuildRequires:  python2-pytest
%endif 
#if with_python2
 
Requires:       python-jinja2
Requires:       python-setuptools
Requires:       python-click

%description
Convert Python packages to RPM SPECFILES. The packages can be downloaded from PyPI and the produced SPEC is in line with Fedora Packaging Guidelines or Mageia Python Policy

%if 0%{?with_python2}
%package -n     python2-%{pypi_name}
Summary:        TODO:
 
Requires:       python-Jinja2
Requires:       python-setuptools
Requires:       python-click

%description -n python2-%{pypi_name}
Convert Python packages to RPM SPECFILES. The packages can be downloaded from PyPI and the produced SPEC is in line with Fedora Packaging Guidelines or Mageia Python Policy
%endif 
#with_python2


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%if 0%{?with_python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

%endif 
#with_python2


%build
%{__python3} setup.py build

%if 0%{?with_python2}
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif 
#with_python2


%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if 0%{?with_python2}
pushd %{py2dir}
%{__python} setup.py install --skip-build --root %{buildroot}
mv %{buildroot}%{_bindir}/pyp2rpm %{buildroot}/%{_bindir}/pyp2rpm-2
popd
%endif 

%{__python3} setup.py install --skip-build --root %{buildroot}


%files
%doc LICENSE
%{_bindir}/pyp2rpm
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%if 0%{?with_python2}
%files -n python-%{pypi_name}
%doc LICENSE
%{_bindir}/pyp2rpm-2
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif 

