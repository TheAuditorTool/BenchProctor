# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify


def BenchmarkTest19853():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(config_value), secure=True, httponly=True, samesite='Strict')
    return resp
