# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest03320():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
