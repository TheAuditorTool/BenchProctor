# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest67603(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
