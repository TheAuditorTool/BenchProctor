# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import importlib


def BenchmarkTest32797():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
