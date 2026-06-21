# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import re
from flask import jsonify
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest06464():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
