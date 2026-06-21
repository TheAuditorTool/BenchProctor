# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest58759():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(comment_value).split(',')
    data = ','.join(parts)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return jsonify({'name': str(value)}), 200
