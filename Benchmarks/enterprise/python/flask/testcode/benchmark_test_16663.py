# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest16663(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
