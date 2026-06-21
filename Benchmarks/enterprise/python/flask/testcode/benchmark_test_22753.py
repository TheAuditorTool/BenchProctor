# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22753():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    eval(str(data))
    return jsonify({"result": "success"})
