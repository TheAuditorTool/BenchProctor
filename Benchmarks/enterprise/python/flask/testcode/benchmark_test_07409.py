# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest07409(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
