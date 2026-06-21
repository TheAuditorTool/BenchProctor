# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest04374():
    origin_value = request.headers.get('Origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
