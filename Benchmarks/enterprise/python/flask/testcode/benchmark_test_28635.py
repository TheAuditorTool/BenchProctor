# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest28635(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
