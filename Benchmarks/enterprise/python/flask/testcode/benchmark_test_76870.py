# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest76870(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
