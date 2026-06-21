# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest32935(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
