# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12195():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    int(str(data))
    return jsonify({"result": "success"})
