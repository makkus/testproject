# Installation

There are three ways to install *testproject* on your machine. Via a manual binary download, an install script, or installation of the python package.

## Binaries

To install `testproject`, download the appropriate binary from one of the links below, and set the downloaded file to be executable (``chmod +x testproject``):

  - [Linux](https://s3-eu-west-1.amazonaws.com/dev.dl.frkl.io/linux-gnu/testproject)
  - [Windows](https://s3-eu-west-1.amazonaws.com/dev.dl.frkl.io/windows/testproject.exe)
  - [Mac OS X](https://s3-eu-west-1.amazonaws.com/dev.dl.frkl.io/darwin/testproject)


## Install script

Alternatively, use the 'curly' install script for `testproject`:

``` console
curl https://gitlab.com/frkl/testproject/-/raw/develop/scripts/install/testproject.sh | bash
```


This will add a section to your shell init file to add the install location (``$HOME/.local/share/frkl/bin``) to your ``$PATH``.

You might need to source that file (or log out and re-log in to your session) in order to be able to use *testproject*:

``` console
source ~/.profile
```


## Python package

The python package is currently not available on [pypi](https://pypi.org), so you need to specify the ``--extra-url`` parameter for your pip command. If you chooose this install method, I assume you know how to install Python packages manually, which is why I only show you an example way of getting *testproject* onto your machine:

``` console
> python3 -m venv ~/.venvs/testproject
> source ~/.venvs/testproject/bin/activate
> pip install --extra-index-url https://pkgs.frkl.io/frkl/dev testproject
Looking in indexes: https://pypi.org/simple, https://pkgs.frkl.io/frkl/dev
Collecting testproject
  Downloading http://pkgs.frkl.io/frkl/dev/%2Bf/ee3/f57bd91a076f9/testproject-0.1.dev24%2Bgd3c4447-py2.py3-none-any.whl (28 kB)
...
...
...
Successfully installed aiokafka-0.6.0 aiopg-1.0.0 ... ... ...
> testproject --help
Usage: testproject [OPTIONS] COMMAND [ARGS]...
   ...
   ...
```
