# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest43645():
    header_value = request.headers.get('X-Custom-Header', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(header_value))
    return resp
