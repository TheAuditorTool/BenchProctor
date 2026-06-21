# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest11121(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
