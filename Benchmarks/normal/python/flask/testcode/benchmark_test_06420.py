# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest06420():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
