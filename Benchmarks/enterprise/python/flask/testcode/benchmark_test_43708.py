# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest43708(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
