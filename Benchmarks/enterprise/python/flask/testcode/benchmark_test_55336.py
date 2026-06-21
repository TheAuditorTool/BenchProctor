# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest55336():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    return str(data), 200, {'Content-Type': 'text/html'}
