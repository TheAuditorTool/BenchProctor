# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify
from app_runtime import db


def BenchmarkTest04697():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(comment_value)
    return jsonify({"result": "success"})
