# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest66246():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
