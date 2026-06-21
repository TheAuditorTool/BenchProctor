# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest62026():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = header_value
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
