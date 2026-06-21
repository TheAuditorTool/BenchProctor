# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from types import SimpleNamespace
from app_runtime import db, auth_check


def BenchmarkTest25996():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
