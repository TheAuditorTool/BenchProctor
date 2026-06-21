# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest65249():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
