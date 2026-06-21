# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


request_state: dict[str, str] = {}

def BenchmarkTest17182():
    referer_value = request.headers.get('Referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
