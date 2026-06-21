# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest68446():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
