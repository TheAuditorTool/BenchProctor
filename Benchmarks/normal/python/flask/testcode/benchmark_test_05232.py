# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def BenchmarkTest05232(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    return Markup('<div>' + str(data) + '</div>')
