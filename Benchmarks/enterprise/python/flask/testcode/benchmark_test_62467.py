# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest62467():
    user_id = request.args.get('id', '')
    data = coalesce_blank(user_id)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
