# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest29646():
    origin_value = request.headers.get('Origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:_?&=\\-@]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return redirect(str(processed))
