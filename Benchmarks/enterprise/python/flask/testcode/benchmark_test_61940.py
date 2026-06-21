# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest61940(path_param):
    path_value = path_param
    data = to_text(path_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
