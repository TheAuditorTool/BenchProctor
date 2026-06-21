# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import redirect
import urllib.parse


request_state: dict[str, str] = {}

def BenchmarkTest28480():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
