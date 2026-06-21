# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest46586(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
