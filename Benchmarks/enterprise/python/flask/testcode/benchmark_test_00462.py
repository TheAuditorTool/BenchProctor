# SPDX-License-Identifier: Apache-2.0
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest00462():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
