# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest40040():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
