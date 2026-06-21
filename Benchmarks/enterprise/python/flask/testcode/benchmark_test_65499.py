# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest65499():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
