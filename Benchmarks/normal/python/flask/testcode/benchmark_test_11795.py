# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest11795(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    return str(data), 200, {'Content-Type': 'text/html'}
