# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def BenchmarkTest63693(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    return Markup('<div>' + str(data) + '</div>')
