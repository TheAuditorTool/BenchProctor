# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest29669():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
