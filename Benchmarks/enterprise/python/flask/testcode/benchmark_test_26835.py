# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote


def BenchmarkTest26835(path_param):
    path_value = path_param
    data = unquote(path_value)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
