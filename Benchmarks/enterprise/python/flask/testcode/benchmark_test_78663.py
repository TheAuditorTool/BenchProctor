# SPDX-License-Identifier: Apache-2.0
import html
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest78663():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    processed = str(data).replace("<script", "")
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
