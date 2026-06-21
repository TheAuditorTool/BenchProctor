# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest29990():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
