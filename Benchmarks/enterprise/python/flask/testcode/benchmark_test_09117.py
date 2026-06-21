# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def ensure_str(value):
    return str(value)

def BenchmarkTest09117():
    ua_value = request.headers.get('User-Agent', '')
    data = ensure_str(ua_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
