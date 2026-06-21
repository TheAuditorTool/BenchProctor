# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote


def BenchmarkTest64792(path_param):
    path_value = path_param
    data = unquote(path_value)
    return str(data), 200, {'Content-Type': 'text/html'}
