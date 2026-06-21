# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


request_state: dict[str, str] = {}

def BenchmarkTest43079():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
