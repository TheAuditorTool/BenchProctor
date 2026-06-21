# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest08754(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
