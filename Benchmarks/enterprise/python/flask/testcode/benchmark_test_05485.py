# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


request_state: dict[str, str] = {}

def BenchmarkTest05485():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
