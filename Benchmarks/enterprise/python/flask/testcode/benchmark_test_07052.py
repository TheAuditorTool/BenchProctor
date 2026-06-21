# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from app_runtime import db, auth_check


def BenchmarkTest07052():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if not auth_check(str(comment_value), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
