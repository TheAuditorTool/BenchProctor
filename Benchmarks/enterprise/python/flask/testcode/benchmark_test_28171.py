# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def BenchmarkTest28171(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    return Markup('<div>' + str(data) + '</div>')
