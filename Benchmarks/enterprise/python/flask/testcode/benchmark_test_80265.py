# SPDX-License-Identifier: Apache-2.0
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest80265():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
