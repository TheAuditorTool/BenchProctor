# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest79569(path_param):
    path_value = path_param
    with open('/var/app/data/' + str(path_value), 'r') as fh:
        content = fh.read()
    return content
