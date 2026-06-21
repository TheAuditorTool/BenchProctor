# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest67049():
    upload_name = request.files['upload'].filename
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(upload_name), secure=True, httponly=True, samesite='Strict')
    return resp
