# SPDX-License-Identifier: Apache-2.0
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest26349():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
