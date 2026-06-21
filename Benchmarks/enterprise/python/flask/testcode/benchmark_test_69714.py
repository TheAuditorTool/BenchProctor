# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest69714():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(comment_value)}
