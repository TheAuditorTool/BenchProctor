# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest18548():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    processed = data[:64]
    return jsonify({'error': str(processed), 'stack': repr(locals())}), 500
