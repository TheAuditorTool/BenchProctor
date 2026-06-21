# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest62216(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
