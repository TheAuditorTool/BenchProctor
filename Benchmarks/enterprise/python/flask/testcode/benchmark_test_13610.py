# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest13610():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '{}'.format(forwarded_ip)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
