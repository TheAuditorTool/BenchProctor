# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest41639():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    session['data'] = str(data)
    return jsonify({"result": "success"})
