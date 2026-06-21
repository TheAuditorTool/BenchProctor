# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest52722():
    user_id = request.args.get('id', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(user_id), secure=True, httponly=True, samesite='Strict')
    return resp
