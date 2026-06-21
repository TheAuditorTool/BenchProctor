# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import pickle


request_state: dict[str, str] = {}

def BenchmarkTest63507():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    pickle.loads(processed.encode('latin-1'))
    return jsonify({"result": "success"})
