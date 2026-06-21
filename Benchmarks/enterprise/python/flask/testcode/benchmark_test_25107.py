# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest25107():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
