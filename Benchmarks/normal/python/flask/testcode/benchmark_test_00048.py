# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def BenchmarkTest00048(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    return Markup('<img src="' + str(data) + '">')
