# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest61435():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
