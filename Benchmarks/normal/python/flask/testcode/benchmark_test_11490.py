# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import importlib


request_state: dict[str, str] = {}

def BenchmarkTest11490():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
