# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest65817():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
