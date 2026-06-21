# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest57658():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = relay_value(comment_value)
    processed = data[:64]
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(processed),))
    return jsonify({'secret': str(secret)}), 200
