# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import jsonify
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest27615():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s<>\\"\'/(){}.*]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
