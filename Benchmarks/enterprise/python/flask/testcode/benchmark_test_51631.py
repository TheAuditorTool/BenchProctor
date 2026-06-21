# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest51631(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
