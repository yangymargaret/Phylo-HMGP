#! /usr/bin/env python
#
# Copyright (C) 2007-2009 Cournapeau David <cournape@gmail.com>
#               2010 Fabian Pedregosa <fabian.pedregosa@inria.fr>
#               2014 Gael Varoquaux
#               2014-2016 Sergei Lebedev <superbobry@gmail.com>

"""Hidden Markov Models in Python with scikit-learn like API"""

import sys

try:
    from numpy.distutils.misc_util import get_info
except ImportError:
    # A dirty hack to get RTD running.
    def get_info(name):
        return {}

from setuptools import setup, Extension

setup_options = dict(
    name="phylo_hmgp",
    description='This is _hmmc module for phylo-hmgp',
    version='1.0',
    ext_modules=[
        Extension("_hmmc", ["_hmmc.c"],
                  extra_compile_args=["-O3"],
                  **get_info("npymath"))
    ]
)

if __name__ == "__main__":
    setup(**setup_options)
