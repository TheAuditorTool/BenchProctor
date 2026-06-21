# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest34956():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if forwarded_ip not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = forwarded_ip
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
