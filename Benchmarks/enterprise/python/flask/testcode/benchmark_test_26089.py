# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest26089():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
