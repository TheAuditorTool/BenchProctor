# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
from flask import session


def BenchmarkTest38651():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = f'{config_value}'
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
