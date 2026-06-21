# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest48258():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    exec(str(processed))
    return jsonify({"result": "success"})
