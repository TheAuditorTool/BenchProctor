# SPDX-License-Identifier: Apache-2.0
from flask import session
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest00790():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session['user'] = str(processed)
    return jsonify({"result": "success"})
