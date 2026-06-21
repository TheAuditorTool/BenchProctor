# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest53768():
    referer_value = request.headers.get('Referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if session.get('role') != 'admin':
        return jsonify({'error': 'forbidden'}), 403
    session['data'] = str(data)
    return jsonify({"result": "success"})
