# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest66856():
    user_id = request.args.get('id', '')
    data = relay_value(user_id)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
