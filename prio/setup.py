# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import setuptools
from distutils.core import setup, Extension
from glob import glob
from os import path
from sys import platform


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


# Add platform specific settings for building the extension module
if platform == "darwin":
    # macOS
    library_dirs = ["/usr/local/opt/nss/lib"]
    include_dirs = [
        "/usr/local/opt/nss/include/nss",
        "/usr/local/opt/nspr/include/nspr",
    ]
else:
    # Fedora
    library_dirs = []
    include_dirs = ["/usr/include/nspr", "/usr/include/nss"]


extension_mod = Extension(
    "_libprio",
    ["libprio_wrap.c"],
    library_dirs=["libprio/build/prio", "libprio/build/mpi"] + library_dirs,
    include_dirs=include_dirs,
    libraries=["mprio", "mpi", "msgpackc", "nss3", "nspr4"],
)

setup(
    name="prio",
    version="0.5",
    description="An interface to libprio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Anthony Miyaguchi",
    author_email="amiyaguchi@mozilla.com",
    url="https://github.com/mozilla/python-libprio",
    entry_points={"console_scripts": ["prio=prio.__main__:main"]},
    install_requires=["click"],
    packages=["prio", "prio.cli"],
    ext_modules=[extension_mod],
)
