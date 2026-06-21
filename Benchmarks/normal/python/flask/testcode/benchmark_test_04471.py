# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def BenchmarkTest04471(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    return Markup('<div>' + str(data) + '</div>')
