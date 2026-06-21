# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest33510():
    ua_value = request.headers.get('User-Agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(processed),))
    return jsonify({"result": "success"})
