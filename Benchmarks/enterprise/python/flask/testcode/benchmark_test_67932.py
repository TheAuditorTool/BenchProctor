# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote


def BenchmarkTest67932(path_param):
    path_value = path_param
    data = unquote(path_value)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
