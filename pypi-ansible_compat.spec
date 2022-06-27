#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ansible_compat
Version  : 2.1.0
Release  : 14
URL      : https://files.pythonhosted.org/packages/5b/51/2ba6b4783de230234e3f289b17c51bda9cd5b10a2392cfcc92c64c98cb7a/ansible-compat-2.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5b/51/2ba6b4783de230234e3f289b17c51bda9cd5b10a2392cfcc92c64c98cb7a/ansible-compat-2.1.0.tar.gz
Summary  : Ansible compatibility goodies
Group    : Development/Tools
License  : MIT
Requires: pypi-ansible_compat-license = %{version}-%{release}
Requires: pypi-ansible_compat-python = %{version}-%{release}
Requires: pypi-ansible_compat-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(alabaster)
BuildRequires : pypi(ansible_pygments)
BuildRequires : pypi(argh)
BuildRequires : pypi(attrs)
BuildRequires : pypi(babel)
BuildRequires : pypi(certifi)
BuildRequires : pypi(charset_normalizer)
BuildRequires : pypi(click)
BuildRequires : pypi(commonmark)
BuildRequires : pypi(coverage)
BuildRequires : pypi(docutils)
BuildRequires : pypi(flaky)
BuildRequires : pypi(idna)
BuildRequires : pypi(imagesize)
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(iniconfig)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(jsonschema)
BuildRequires : pypi(livereload)
BuildRequires : pypi(markdown_it_py)
BuildRequires : pypi(markupsafe)
BuildRequires : pypi(mdit_py_plugins)
BuildRequires : pypi(mdurl)
BuildRequires : pypi(more_itertools)
BuildRequires : pypi(myst_parser)
BuildRequires : pypi(packaging)
BuildRequires : pypi(pathtools)
BuildRequires : pypi(pep517)
BuildRequires : pypi(pip_tools)
BuildRequires : pypi(pluggy)
BuildRequires : pypi(port_for)
BuildRequires : pypi(py)
BuildRequires : pypi(pygments)
BuildRequires : pypi(pyparsing)
BuildRequires : pypi(pyrsistent)
BuildRequires : pypi(pytz)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(requests)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(setuptools_scm_git_archive)
BuildRequires : pypi(six)
BuildRequires : pypi(snowballstemmer)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(sphinx_ansible_theme)
BuildRequires : pypi(sphinx_autobuild)
BuildRequires : pypi(sphinx_rtd_theme)
BuildRequires : pypi(sphinxcontrib_applehelp)
BuildRequires : pypi(sphinxcontrib_devhelp)
BuildRequires : pypi(sphinxcontrib_htmlhelp)
BuildRequires : pypi(sphinxcontrib_jsmath)
BuildRequires : pypi(sphinxcontrib_qthelp)
BuildRequires : pypi(sphinxcontrib_serializinghtml)
BuildRequires : pypi(subprocess_tee)
BuildRequires : pypi(toml)
BuildRequires : pypi(tomli)
BuildRequires : pypi(tornado)
BuildRequires : pypi(typing_extensions)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(watchdog)
BuildRequires : pypi(wheel)
BuildRequires : pypi(zipp)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
# ansible-compat
[![pypi](https://img.shields.io/pypi/v/ansible-compat.svg)](https://pypi.org/project/ansible-compat/)
[![docs](https://readthedocs.org/projects/ansible-compat/badge/?version=latest)](https://ansible-compat.readthedocs.io/en/latest/)
[![gh](https://github.com/ansible-community/ansible-compat/actions/workflows/tox.yml/badge.svg)](https://github.com/ansible-community/ansible-compat/actions/workflows/tox.yml)
[![codecov.io](https://codecov.io/github/ansible-community/ansible-compat/coverage.svg?branch=main)](https://codecov.io/github/ansible-community/ansible-compat?branch=main)

%package license
Summary: license components for the pypi-ansible_compat package.
Group: Default

%description license
license components for the pypi-ansible_compat package.


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
Requires: pypi(alabaster)
Requires: pypi(ansible_pygments)
Requires: pypi(argh)
Requires: pypi(attrs)
Requires: pypi(babel)
Requires: pypi(certifi)
Requires: pypi(charset_normalizer)
Requires: pypi(click)
Requires: pypi(commonmark)
Requires: pypi(coverage)
Requires: pypi(docutils)
Requires: pypi(flaky)
Requires: pypi(idna)
Requires: pypi(imagesize)
Requires: pypi(importlib_metadata)
Requires: pypi(iniconfig)
Requires: pypi(jinja2)
Requires: pypi(jsonschema)
Requires: pypi(livereload)
Requires: pypi(markdown_it_py)
Requires: pypi(markupsafe)
Requires: pypi(mdit_py_plugins)
Requires: pypi(mdurl)
Requires: pypi(more_itertools)
Requires: pypi(myst_parser)
Requires: pypi(packaging)
Requires: pypi(pathtools)
Requires: pypi(pep517)
Requires: pypi(pip_tools)
Requires: pypi(pluggy)
Requires: pypi(port_for)
Requires: pypi(py)
Requires: pypi(pygments)
Requires: pypi(pyparsing)
Requires: pypi(pyrsistent)
Requires: pypi(pytz)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(six)
Requires: pypi(snowballstemmer)
Requires: pypi(sphinx)
Requires: pypi(sphinx_ansible_theme)
Requires: pypi(sphinx_autobuild)
Requires: pypi(sphinx_rtd_theme)
Requires: pypi(sphinxcontrib_applehelp)
Requires: pypi(sphinxcontrib_devhelp)
Requires: pypi(sphinxcontrib_htmlhelp)
Requires: pypi(sphinxcontrib_jsmath)
Requires: pypi(sphinxcontrib_qthelp)
Requires: pypi(sphinxcontrib_serializinghtml)
Requires: pypi(subprocess_tee)
Requires: pypi(toml)
Requires: pypi(tomli)
Requires: pypi(tornado)
Requires: pypi(typing_extensions)
Requires: pypi(urllib3)
Requires: pypi(watchdog)
Requires: pypi(zipp)

%description python3
python3 components for the pypi-ansible_compat package.


%prep
%setup -q -n ansible-compat-2.1.0
cd %{_builddir}/ansible-compat-2.1.0
pushd ..
cp -a ansible-compat-2.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656355347
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
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ansible_compat
cp %{_builddir}/ansible-compat-2.1.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ansible_compat/6d176c0e7c1be160c6ae0a7d0aa5f51a4142177e
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ansible_compat/6d176c0e7c1be160c6ae0a7d0aa5f51a4142177e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
