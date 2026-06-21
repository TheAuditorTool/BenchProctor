# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def BenchmarkTest22276(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    return Markup('<div>' + str(data) + '</div>')
