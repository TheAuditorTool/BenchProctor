# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest02469():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    return str(data), 200, {'Content-Type': 'text/html'}
