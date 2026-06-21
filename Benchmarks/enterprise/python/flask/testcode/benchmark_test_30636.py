# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest30636():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    return str(data), 200, {'Content-Type': 'text/html'}
