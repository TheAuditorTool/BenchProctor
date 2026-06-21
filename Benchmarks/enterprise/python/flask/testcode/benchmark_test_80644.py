# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest80644():
    upload_name = request.files['upload'].filename
    data = relay_value(upload_name)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
