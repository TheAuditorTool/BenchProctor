# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest58414():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    processed = data[:64]
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
