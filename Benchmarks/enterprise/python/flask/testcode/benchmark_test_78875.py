# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest78875():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
