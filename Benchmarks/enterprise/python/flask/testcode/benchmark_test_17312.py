# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest17312(path_param):
    path_value = path_param
    data = f'{path_value}'
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
