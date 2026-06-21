# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest59119():
    host_value = request.headers.get('Host', '')
    data = coalesce_blank(host_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
