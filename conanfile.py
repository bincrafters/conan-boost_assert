#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostAssertConan(base.BoostBaseConan):
    name = "boost_assert"
    url = "https://github.com/bincrafters/conan-boost_assert"
    lib_short_names = ["assert"]
    header_only_libs = ["assert"]
    b2_requires = [
        "boost_config",
    ]


