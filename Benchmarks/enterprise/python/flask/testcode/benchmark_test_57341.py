# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest57341():
    user_id = request.args.get('id', '')
    data = default_blank(user_id)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
