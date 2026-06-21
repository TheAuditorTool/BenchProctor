# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest66501(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
