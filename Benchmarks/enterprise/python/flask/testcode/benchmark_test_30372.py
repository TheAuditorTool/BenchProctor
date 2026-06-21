# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest30372(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    return str(data), 200, {'Content-Type': 'text/html'}
