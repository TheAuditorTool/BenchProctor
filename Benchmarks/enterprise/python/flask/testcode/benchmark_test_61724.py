# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest61724():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
