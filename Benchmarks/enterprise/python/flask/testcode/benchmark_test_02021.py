# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest02021():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
