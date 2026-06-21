# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest56591():
    origin_value = request.headers.get('Origin', '')
    if origin_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = origin_value
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
