# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest25944():
    upload_name = request.files['upload'].filename
    data = normalise_input(upload_name)
    if str(data).lower() not in ('true', 'false'):
        return jsonify({'error': 'invalid boolean'}), 400
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
