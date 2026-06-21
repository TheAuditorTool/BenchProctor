# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest45719(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
