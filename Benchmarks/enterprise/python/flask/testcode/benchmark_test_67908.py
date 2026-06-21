# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from app_runtime import db, auth_check


def BenchmarkTest67908():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(comment_value)
    data = collected
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
