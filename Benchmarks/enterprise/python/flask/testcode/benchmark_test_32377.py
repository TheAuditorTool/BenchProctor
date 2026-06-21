# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest32377():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(graphql_var), secure=True, httponly=True, samesite='Strict')
    return resp
