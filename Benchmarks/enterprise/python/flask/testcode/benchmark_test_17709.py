# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest17709():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
