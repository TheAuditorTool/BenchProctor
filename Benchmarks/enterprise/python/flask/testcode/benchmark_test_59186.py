# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest59186():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
