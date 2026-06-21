# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote


def BenchmarkTest10967(path_param):
    path_value = path_param
    data = unquote(path_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
