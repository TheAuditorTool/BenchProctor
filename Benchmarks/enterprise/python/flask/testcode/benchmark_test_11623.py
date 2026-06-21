# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from urllib.parse import unquote


def BenchmarkTest11623(path_param):
    path_value = path_param
    data = unquote(path_value)
    return Markup('<div>' + str(data) + '</div>')
