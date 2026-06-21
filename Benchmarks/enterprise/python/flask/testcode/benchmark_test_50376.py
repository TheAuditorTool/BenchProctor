# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest50376():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = comment_value
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
