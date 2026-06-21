# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest04948(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
