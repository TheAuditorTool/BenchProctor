# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
from app_runtime import db


def BenchmarkTest07087():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(comment_value), secure=True, httponly=True, samesite='Strict')
    return resp
