#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import platform
import os

from bincrafters import build_template_default


def download(url, filename):
    try:
        from urllib.request import urlretrieve
        from urllib.parse import urlparse
    except ImportError:
        from urllib import urlretrieve
        from urlparse import urlparse

    urlretrieve(url, filename)


if __name__ == "__main__":

    base = "https://raw.githubusercontent.com/conan-io/conan-center-index/master/recipes/brotli/all/"
    download(base + "conanfile.py", "conanfile.py")
    download(base + "conandata.yml", "conandata.yml")
    download(base + "CMakeLists.txt", "CMakeLists.txt")
    os.makedirs("test_package")
    download(base + "test_package/CMakeLists.txt", "test_package/CMakeLists.txt")
    download(base + "test_package/conanfile.py", "test_package/conanfile.py")
    download(base + "test_package/test_package.cpp", "test_package/test_package.cpp")

    builder = build_template_default.get_builder(pure_c=True)

    items = []
    for item in builder.items:
        if item.options["brotli:shared"] == True:
            items.append(item)
    builder.items = items

    builder.run()
