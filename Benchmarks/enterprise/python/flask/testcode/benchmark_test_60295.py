# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def BenchmarkTest60295(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    return Markup('<div>' + str(data) + '</div>')
