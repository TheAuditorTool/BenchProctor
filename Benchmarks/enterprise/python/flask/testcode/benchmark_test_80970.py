# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest80970():
    raw_body = request.get_data(as_text=True)
    data = normalise_input(raw_body)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
