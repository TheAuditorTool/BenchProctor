# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest23153(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
