# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from app_runtime import db, auth_check


def BenchmarkTest12202():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value != session.get('csrf_token'):
        return jsonify({'error': 'CSRF token mismatch'}), 403
    if not auth_check(session.get('user', ''), str(comment_value)):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
