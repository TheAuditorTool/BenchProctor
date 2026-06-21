# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest76954():
    origin_value = request.headers.get('Origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    if str(processed).startswith('https://admin.internal/'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
