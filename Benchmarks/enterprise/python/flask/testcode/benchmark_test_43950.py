# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest43950():
    auth_header = request.headers.get('Authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
