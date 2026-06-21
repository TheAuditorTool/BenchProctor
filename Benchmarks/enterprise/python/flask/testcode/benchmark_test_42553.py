# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def coalesce_blank(value):
    return value or ''

def BenchmarkTest42553():
    user_id = request.args.get('id', '')
    data = coalesce_blank(user_id)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
