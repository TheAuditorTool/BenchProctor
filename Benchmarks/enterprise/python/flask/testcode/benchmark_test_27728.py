# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest27728():
    user_id = request.args.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
