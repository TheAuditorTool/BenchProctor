# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest15542():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    data = bytearray(int(processed) if str(processed).isdigit() else 0)
    return jsonify({"result": "success"})
