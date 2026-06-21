# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest61301():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    return jsonify({'error': str(comment_value), 'stack': repr(locals())}), 500
