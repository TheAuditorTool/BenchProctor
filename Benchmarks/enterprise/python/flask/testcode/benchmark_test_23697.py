# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest23697(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
