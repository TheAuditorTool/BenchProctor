# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest48711():
    cookie_value = request.cookies.get('session_token', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(cookie_value), max_age=86400)
    return resp
