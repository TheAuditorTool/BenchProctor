# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest75144(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
