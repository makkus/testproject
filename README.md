[![PyPI status](https://img.shields.io/pypi/status/testproject.svg)](https://pypi.python.org/pypi/testproject/)
[![PyPI version](https://img.shields.io/pypi/v/testproject.svg)](https://pypi.python.org/pypi/testproject/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/testproject.svg)](https://pypi.python.org/pypi/testproject/)
[![Pipeline status](https://gitlab.com/frkl/testproject/badges/develop/pipeline.svg)](https://gitlab.com/frkl/testproject/pipelines)
[![coverage report](https://gitlab.com/frkl/testproject/badges/develop/coverage.svg)](https://gitlab.com/frkl/testproject/-/commits/develop)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# testproject

*asdf*


## Description

Documentation still to be done.


## Downloads

### Binaries

  - [Linux](https://s3-eu-west-1.amazonaws.com/dev.dl.frkl.io/linux-gnu/testproject)
  - [Windows](https://s3-eu-west-1.amazonaws.com/dev.dl.frkl.io/windows/testproject.exe)
  - [Mac OS X](https://s3-eu-west-1.amazonaws.com/dev.dl.frkl.io/darwin/testproject)


# Development

## Requirements

- Python (version >=3.6)
- pip, virtualenv
- git
- make
- [direnv](https://direnv.net/) (optional)


## Prepare development environment

Notes:

- if using *direnv*, adjust the Python version in ``.envrc`` (should not be necessary)
- if not using *direnv*, you have to setup and activate your Python virtualenv yourself, manually, before running ``make init``

``` console
git clone https://gitlab.com/frkl/testproject
cd testproject
mv .envrc.disabled .envrc
direnv allow   # if using direnv, otherwise activate virtualenv
make init
```


## ``make`` targets

- ``init``: init development project (install project & dev dependencies into virtualenv, as well as pre-commit git hook)
- ``binary``: create binary for project (will install *pyenv* -- check ``scripts/build-binary`` for details)
- ``flake``: run *flake8* tests
- ``mypy``: run mypy tests
- ``test``: run unit tests
- ``docs``: create static documentation pages
- ``serve-docs``: serve documentation pages (incl. auto-reload)
- ``clean``: clean build directories

For details (and other, minor targets), check the ``Makefile``.


## Running tests

``` console
> make test
# or
> make coverage
```


## Update project template

This project uses [cruft](https://github.com/timothycrosley/cruft) to apply updates to [the base Python project template](https://gitlab.com/frkl/template-python-project) to this repository. Check out it's documentation for more information.

``` console
cruft update
# interactively approve changes, make changes if necessary
git add *
git commit -m "chore: updated project from template"
```


## Copyright & license

Please check the [LICENSE](/LICENSE) file in this repository (it's a short license!).

[Parity Public License 6.0.0](https://licensezero.com/licenses/parity)

[Copyright (c) 2020 frkl OÜ](https://frkl.io)
