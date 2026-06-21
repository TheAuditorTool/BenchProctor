# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest20074():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
