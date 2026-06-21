# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest01739():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
