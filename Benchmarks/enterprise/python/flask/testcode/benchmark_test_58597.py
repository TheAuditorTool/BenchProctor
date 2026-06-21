# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest58597():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(forwarded_ip))
    return resp
