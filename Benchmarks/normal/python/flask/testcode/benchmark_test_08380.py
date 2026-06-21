# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


request_state: dict[str, str] = {}

def BenchmarkTest08380():
    upload_name = request.files['upload'].filename
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
