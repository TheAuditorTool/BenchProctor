# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest60720():
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
