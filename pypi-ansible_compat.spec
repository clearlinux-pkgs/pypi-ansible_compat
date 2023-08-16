#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-ansible_compat
Version  : 4.1.6
Release  : 33
URL      : https://files.pythonhosted.org/packages/96/00/f6354ed2fde456bbec306fcebd27f3282d6d19ba4b0f6aa3637657295d28/ansible-compat-4.1.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/96/00/f6354ed2fde456bbec306fcebd27f3282d6d19ba4b0f6aa3637657295d28/ansible-compat-4.1.6.tar.gz
Summary  : Ansible compatibility goodies
Group    : Development/Tools
License  : MIT
Requires: pypi-ansible_compat-license = %{version}-%{release}
Requires: pypi-ansible_compat-python = %{version}-%{release}
Requires: pypi-ansible_compat-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(argparse_manpage)
BuildRequires : pypi(attrs)
BuildRequires : pypi(beautifulsoup4)
BuildRequires : pypi(black)
BuildRequires : pypi(build)
BuildRequires : pypi(cairocffi)
BuildRequires : pypi(cairosvg)
BuildRequires : pypi(certifi)
BuildRequires : pypi(cffi)
BuildRequires : pypi(charset_normalizer)
BuildRequires : pypi(click)
BuildRequires : pypi(colorama)
BuildRequires : pypi(coverage)
BuildRequires : pypi(cryptography)
BuildRequires : pypi(csscompressor)
BuildRequires : pypi(cssselect2)
BuildRequires : pypi(defusedxml)
BuildRequires : pypi(exceptiongroup)
BuildRequires : pypi(ghp_import)
BuildRequires : pypi(griffe)
BuildRequires : pypi(idna)
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(importlib_resources)
BuildRequires : pypi(iniconfig)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(jsmin)
BuildRequires : pypi(jsonschema)
BuildRequires : pypi(markdown)
BuildRequires : pypi(markdown_exec)
BuildRequires : pypi(markdown_include)
BuildRequires : pypi(markupsafe)
BuildRequires : pypi(mergedeep)
BuildRequires : pypi(mkdocs)
BuildRequires : pypi(mkdocs_autorefs)
BuildRequires : pypi(mkdocs_gen_files)
BuildRequires : pypi(mkdocs_htmlproofer_plugin)
BuildRequires : pypi(mkdocs_material_extensions)
BuildRequires : pypi(mkdocs_monorepo_plugin)
BuildRequires : pypi(mkdocstrings)
BuildRequires : pypi(mkdocstrings_python)
BuildRequires : pypi(mypy_extensions)
BuildRequires : pypi(packaging)
BuildRequires : pypi(pathspec)
BuildRequires : pypi(pillow)
BuildRequires : pypi(pip)
BuildRequires : pypi(pip_tools)
BuildRequires : pypi(pipdeptree)
BuildRequires : pypi(platformdirs)
BuildRequires : pypi(pluggy)
BuildRequires : pypi(py)
BuildRequires : pypi(pycparser)
BuildRequires : pypi(pygments)
BuildRequires : pypi(pymdown_extensions)
BuildRequires : pypi(pyproject_hooks)
BuildRequires : pypi(pyrsistent)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(python_slugify)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(pyyaml_env_tag)
BuildRequires : pypi(regex)
BuildRequires : pypi(requests)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(six)
BuildRequires : pypi(soupsieve)
BuildRequires : pypi(subprocess_tee)
BuildRequires : pypi(text_unidecode)
BuildRequires : pypi(tinycss2)
BuildRequires : pypi(toml)
BuildRequires : pypi(tomli)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(watchdog)
BuildRequires : pypi(webencodings)
BuildRequires : pypi(wheel)
BuildRequires : pypi(zipp)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# ansible-compat
[![pypi](https://img.shields.io/pypi/v/ansible-compat.svg)](https://pypi.org/project/ansible-compat/)
[![docs](https://readthedocs.org/projects/ansible-compat/badge/?version=latest)](https://ansible-compat.readthedocs.io/)
[![gh](https://github.com/ansible/ansible-compat/actions/workflows/tox.yml/badge.svg)](https://github.com/ansible/ansible-compat/actions/workflows/tox.yml)
[![codecov.io](https://codecov.io/github/ansible/ansible-compat/coverage.svg?branch=main)](https://codecov.io/github/ansible/ansible-compat?branch=main)

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
Requires: pypi(ansible_core)
Requires: pypi(argparse_manpage)
Requires: pypi(attrs)
Requires: pypi(beautifulsoup4)
Requires: pypi(black)
Requires: pypi(build)
Requires: pypi(cairocffi)
Requires: pypi(cairosvg)
Requires: pypi(certifi)
Requires: pypi(cffi)
Requires: pypi(charset_normalizer)
Requires: pypi(click)
Requires: pypi(colorama)
Requires: pypi(coverage)
Requires: pypi(cryptography)
Requires: pypi(csscompressor)
Requires: pypi(cssselect2)
Requires: pypi(defusedxml)
Requires: pypi(exceptiongroup)
Requires: pypi(ghp_import)
Requires: pypi(griffe)
Requires: pypi(idna)
Requires: pypi(importlib_metadata)
Requires: pypi(importlib_resources)
Requires: pypi(iniconfig)
Requires: pypi(jinja2)
Requires: pypi(jsmin)
Requires: pypi(jsonschema)
Requires: pypi(markdown)
Requires: pypi(markdown_exec)
Requires: pypi(markdown_include)
Requires: pypi(markupsafe)
Requires: pypi(mergedeep)
Requires: pypi(mkdocs)
Requires: pypi(mkdocs_autorefs)
Requires: pypi(mkdocs_gen_files)
Requires: pypi(mkdocs_htmlproofer_plugin)
Requires: pypi(mkdocs_material_extensions)
Requires: pypi(mkdocs_monorepo_plugin)
Requires: pypi(mkdocstrings)
Requires: pypi(mkdocstrings_python)
Requires: pypi(mypy_extensions)
Requires: pypi(packaging)
Requires: pypi(pathspec)
Requires: pypi(pillow)
Requires: pypi(pip)
Requires: pypi(pip_tools)
Requires: pypi(pipdeptree)
Requires: pypi(platformdirs)
Requires: pypi(pluggy)
Requires: pypi(pycparser)
Requires: pypi(pygments)
Requires: pypi(pymdown_extensions)
Requires: pypi(pyproject_hooks)
Requires: pypi(pyrsistent)
Requires: pypi(python_dateutil)
Requires: pypi(python_slugify)
Requires: pypi(pyyaml)
Requires: pypi(pyyaml_env_tag)
Requires: pypi(regex)
Requires: pypi(requests)
Requires: pypi(six)
Requires: pypi(soupsieve)
Requires: pypi(subprocess_tee)
Requires: pypi(text_unidecode)
Requires: pypi(tinycss2)
Requires: pypi(toml)
Requires: pypi(tomli)
Requires: pypi(urllib3)
Requires: pypi(watchdog)
Requires: pypi(webencodings)
Requires: pypi(wheel)
Requires: pypi(zipp)

%description python3
python3 components for the pypi-ansible_compat package.


%prep
%setup -q -n ansible-compat-4.1.6
cd %{_builddir}/ansible-compat-4.1.6
pushd ..
cp -a ansible-compat-4.1.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692230224
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ansible_compat
cp %{_builddir}/ansible-compat-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ansible_compat/6d176c0e7c1be160c6ae0a7d0aa5f51a4142177e || :
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
