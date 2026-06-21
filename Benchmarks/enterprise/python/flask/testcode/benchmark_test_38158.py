# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest38158():
    host_value = request.headers.get('Host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
