# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify
from app_runtime import db


def BenchmarkTest06368():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = str(comment_value).replace('\x00', '')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
