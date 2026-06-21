# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def BenchmarkTest14983(path_param):
    path_value = path_param
    return Markup('<img src="' + str(path_value) + '">')
