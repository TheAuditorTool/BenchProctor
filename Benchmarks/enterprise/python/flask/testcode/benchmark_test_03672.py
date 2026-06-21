# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03672():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    eval(str(graphql_var))
    return jsonify({"result": "success"})
