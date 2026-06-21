# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest05737(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
