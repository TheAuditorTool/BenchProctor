# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest07193():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = ua_value
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
