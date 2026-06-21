# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest27898():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
