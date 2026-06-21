# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


request_state: dict[str, str] = {}

def BenchmarkTest09077():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
