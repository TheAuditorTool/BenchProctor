# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81476():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ','.join(parts)
    eval(str(data))
    return jsonify({"result": "success"})
