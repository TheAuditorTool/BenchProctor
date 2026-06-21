# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54461():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    if not str(graphql_var).isdigit():
        raise ValueError('invalid input: ' + str(graphql_var))
    return jsonify({"result": "success"})
