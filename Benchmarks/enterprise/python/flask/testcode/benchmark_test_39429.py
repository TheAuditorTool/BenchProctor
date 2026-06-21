# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest39429():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ensure_str(comment_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
