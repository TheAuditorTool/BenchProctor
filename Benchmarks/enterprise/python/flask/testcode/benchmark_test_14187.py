# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest14187(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    return str(data), 200, {'Content-Type': 'text/html'}
