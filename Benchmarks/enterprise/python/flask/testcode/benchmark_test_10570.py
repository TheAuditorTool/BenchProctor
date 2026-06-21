# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest10570(path_param):
    path_value = path_param
    with open(os.path.join('/var/app/data', str(path_value)), 'r') as fh:
        content = fh.read()
    return content
