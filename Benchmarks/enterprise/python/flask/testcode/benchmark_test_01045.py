# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import os
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest01045():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
