# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest16387():
    upload_name = request.files['upload'].filename
    data = coalesce_blank(upload_name)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
