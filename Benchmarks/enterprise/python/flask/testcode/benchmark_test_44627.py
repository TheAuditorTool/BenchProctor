# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest44627():
    ua_value = request.headers.get('User-Agent', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(ua_value))
    return resp
