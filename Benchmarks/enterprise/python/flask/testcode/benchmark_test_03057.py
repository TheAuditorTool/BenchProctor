# SPDX-License-Identifier: Apache-2.0
from flask import request


def ensure_str(value):
    return str(value)

def BenchmarkTest03057():
    origin_value = request.headers.get('Origin', '')
    data = ensure_str(origin_value)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
