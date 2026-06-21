# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest81219(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
