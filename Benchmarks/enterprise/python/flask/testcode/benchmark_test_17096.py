# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from app_runtime import db


def BenchmarkTest17096():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data, _sep, _rest = str(comment_value).partition('\x00')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
