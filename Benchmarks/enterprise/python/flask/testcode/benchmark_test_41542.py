# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from app_runtime import db, auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest41542():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    if data != session.get('csrf_token'):
        return jsonify({'error': 'CSRF token mismatch'}), 403
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
