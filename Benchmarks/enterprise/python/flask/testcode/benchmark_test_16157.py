# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest16157(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    return str(data), 200, {'Content-Type': 'text/html'}
