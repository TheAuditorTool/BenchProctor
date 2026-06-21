# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest11043(path_param):
    path_value = path_param
    data = ensure_str(path_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
