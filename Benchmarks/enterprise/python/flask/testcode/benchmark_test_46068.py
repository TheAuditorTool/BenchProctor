# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest46068():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    try:
        float(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid number'}), 400
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
