# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest01027():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
