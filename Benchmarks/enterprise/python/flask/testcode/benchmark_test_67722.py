# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


request_state: dict[str, str] = {}

def BenchmarkTest67722():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
