# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66881():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    if not str(graphql_var).isdigit():
        raise Exception('error: ' + str(graphql_var))
    return jsonify({"result": "success"})
