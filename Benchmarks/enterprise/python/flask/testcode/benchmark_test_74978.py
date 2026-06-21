# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest74978(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    return str(data), 200, {'Content-Type': 'text/html'}
