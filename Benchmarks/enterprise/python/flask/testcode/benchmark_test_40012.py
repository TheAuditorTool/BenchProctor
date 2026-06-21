# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest40012():
    user_id = request.args.get('id', '')
    if user_id not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = user_id
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
