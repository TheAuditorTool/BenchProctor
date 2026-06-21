# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


def BenchmarkTest64162(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
