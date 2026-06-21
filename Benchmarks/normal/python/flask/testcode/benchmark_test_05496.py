# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest05496():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = normalise_input(comment_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(processed),))
    return jsonify({'record': str(record)}), 200
