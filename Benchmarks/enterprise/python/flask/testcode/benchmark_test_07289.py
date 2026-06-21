# SPDX-License-Identifier: Apache-2.0
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest07289():
    raw_body = request.get_data(as_text=True)
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    return str(data), 200, {'Content-Type': 'text/html'}
