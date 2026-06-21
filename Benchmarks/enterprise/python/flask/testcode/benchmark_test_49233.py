# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest49233():
    origin_value = request.headers.get('Origin', '')
    data = str(origin_value).replace('\x00', '')
    return str(data), 200, {'Content-Type': 'text/html'}
