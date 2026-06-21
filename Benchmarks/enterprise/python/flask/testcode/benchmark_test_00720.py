# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest00720():
    ua_value = request.headers.get('User-Agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(processed)}
