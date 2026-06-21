# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest27708():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(processed))
    return resp
