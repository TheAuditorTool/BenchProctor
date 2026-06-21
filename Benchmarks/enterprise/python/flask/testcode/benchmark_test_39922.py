# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest39922(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    return str(data), 200, {'Content-Type': 'text/html'}
