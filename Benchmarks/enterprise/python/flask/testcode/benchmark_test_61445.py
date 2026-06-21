# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
from app_runtime import db, auth_check


def BenchmarkTest61445():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = (lambda v: v.strip())(comment_value)
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
