# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest59600(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
