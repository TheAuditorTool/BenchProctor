# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest05844():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    return str(data), 200, {'Content-Type': 'text/html'}
