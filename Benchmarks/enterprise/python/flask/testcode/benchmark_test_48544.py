# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def BenchmarkTest48544(path_param):
    path_value = path_param
    data = f'{path_value}'
    return Markup('<div>' + str(data) + '</div>')
