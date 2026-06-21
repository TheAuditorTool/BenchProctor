# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64592():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = f'{graphql_var}'
    int(str(data))
    return jsonify({"result": "success"})
