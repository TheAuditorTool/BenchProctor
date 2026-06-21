# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest10732():
    raw_body = request.get_data(as_text=True)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(raw_body))
    return resp
