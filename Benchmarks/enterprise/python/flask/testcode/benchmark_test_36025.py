# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest36025():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
