# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest05315():
    referer_value = request.headers.get('Referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    _resp = requests.get(str(processed))
    exec(_resp.text)
    return jsonify({"result": "success"})
