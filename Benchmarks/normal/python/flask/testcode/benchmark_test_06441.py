# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest06441():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
