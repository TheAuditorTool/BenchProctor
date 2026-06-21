# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest51654():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
