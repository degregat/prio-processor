# python-libprio

This module contains the Python wrapper around libprio.

```bash
pip install prio
```

## Build and Development

The `libprio` submodule must be initialized before building. Run the following
command to initialize the modules.

```bash
git submodule update --init
```

### Local

Refer to the Dockerfile and the `libprio` submodule for dependencies. If you are
running on macOS, the packages can be installed via homebrew.

```bash
brew install nss nspr scons msgpack swig
```

First, the static libraries for Prio and big numbers are generated in the git
submodule. Then, SWIG generates C files from the SWIG interface file. This
contains the code for sharing data between the static library and Python
objects. Finally, the library is made available to the Python package in an
extension module.

```bash
make
make test
```

### Notes

`libprio` is compiled with position-independent code (`fPIC`).
This is required for the python foreign-function interface.