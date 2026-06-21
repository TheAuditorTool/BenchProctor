# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest17541(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
