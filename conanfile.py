#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostAssertConan(base.BoostBaseConan):
    name = "boost_assert"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_assert"
    lib_short_names = ["assert"]
    header_only_libs = ["assert"]
    b2_requires = ["boost_config"]
