# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest70600():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    if str(data).lower() not in ('true', 'false'):
        return jsonify({'error': 'invalid boolean'}), 400
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
