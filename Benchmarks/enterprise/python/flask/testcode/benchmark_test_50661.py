# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest50661():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
