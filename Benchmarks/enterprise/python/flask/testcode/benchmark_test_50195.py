# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import base64
from flask import request, jsonify


def BenchmarkTest50195():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
