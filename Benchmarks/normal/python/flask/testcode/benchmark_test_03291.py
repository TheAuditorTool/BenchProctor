# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest03291(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
