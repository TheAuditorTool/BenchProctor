# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest54632():
    header_value = request.headers.get('X-Custom-Header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return jsonify({'name': str(value)}), 200
