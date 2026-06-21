# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest01478():
    auth_header = request.headers.get('Authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    arr = [10, 20, 30, 40, 50]
    idx = int(str(processed))
    return jsonify({'lookup': arr[idx]}), 200
