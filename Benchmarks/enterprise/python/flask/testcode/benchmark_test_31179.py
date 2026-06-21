# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest31179():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ensure_str(comment_value)
    return jsonify({'error': 'An internal error occurred'}), 500
