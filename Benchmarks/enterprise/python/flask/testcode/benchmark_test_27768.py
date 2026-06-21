# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest27768(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
