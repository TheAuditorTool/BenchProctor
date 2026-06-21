# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest10656():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
