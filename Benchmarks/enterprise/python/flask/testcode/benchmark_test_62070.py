# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest62070():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value}'
    return str(data), 200, {'Content-Type': 'text/html'}
