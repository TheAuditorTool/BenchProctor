# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def relay_value(value):
    return value

def BenchmarkTest46666():
    auth_header = request.headers.get('Authorization', '')
    data = relay_value(auth_header)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
