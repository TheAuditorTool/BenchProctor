# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest48275(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
