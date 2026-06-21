# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest17212():
    header_value = request.headers.get('X-Custom-Header', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    return str(data), 200, {'Content-Type': 'text/html'}
