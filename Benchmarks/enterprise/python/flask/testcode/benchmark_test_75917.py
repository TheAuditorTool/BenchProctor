# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest75917():
    host_value = request.headers.get('Host', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
