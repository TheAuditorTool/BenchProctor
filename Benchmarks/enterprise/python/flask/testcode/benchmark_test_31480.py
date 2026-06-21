# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest31480():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    os.remove(str(data))
    return jsonify({"result": "success"})
