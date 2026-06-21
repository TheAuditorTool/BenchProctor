# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest08816():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(comment_value),))
    value = result['name']
    return jsonify({'name': str(value)}), 200
