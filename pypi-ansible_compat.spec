#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ansible_compat
Version  : 0.5.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/de/be/d2922db62b403b0232743da47b043bdc74312c8cb401383bd37a43dc27cf/ansible-compat-0.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/de/be/d2922db62b403b0232743da47b043bdc74312c8cb401383bd37a43dc27cf/ansible-compat-0.5.0.tar.gz
Summary  : Ansible compatibility goodies
Group    : Development/Tools
License  : MIT
Requires: pypi-ansible_compat-python = %{version}-%{release}
Requires: pypi-ansible_compat-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(setuptools_scm_git_archive)
BuildRequires : pypi(wheel)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
# ansible-compat
[![pypi](https://img.shields.io/pypi/v/ansible-compat.svg)](https://pypi.org/project/ansible-compat/)
[![docs](https://readthedocs.org/projects/ansible-compat/badge/?version=latest)](https://ansible-compat.readthedocs.io/en/latest/)
[![gh](https://github.com/ansible-community/ansible-compat/actions/workflows/tox.yml/badge.svg)](https://github.com/ansible-community/ansible-compat/actions/workflows/tox.yml)
[![codecov.io](https://codecov.io/github/ansible-community/ansible-compat/coverage.svg?branch=main)](https://codecov.io/github/ansible-community/ansible-compat?branch=main)

%package python
Summary: python components for the pypi-ansible_compat package.
Group: Default
Requires: pypi-ansible_compat-python3 = %{version}-%{release}

%description python
python components for the pypi-ansible_compat package.


%package python3
Summary: python3 components for the pypi-ansible_compat package.
Group: Default
Requires: python3-core
Provides: pypi(ansible_compat)
Requires: pypi(pyyaml)

%description python3
python3 components for the pypi-ansible_compat package.


%prep
%setup -q -n ansible-compat-0.5.0
cd %{_builddir}/ansible-compat-0.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639044658
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
