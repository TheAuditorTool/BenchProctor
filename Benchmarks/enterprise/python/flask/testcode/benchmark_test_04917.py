# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest04917():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    def normalize(value):
        return value.strip()
    data = normalize(graphql_var)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
