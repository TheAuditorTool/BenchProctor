# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26163():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    int(str(graphql_var))
    return jsonify({"result": "success"})
