# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59241():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    eval(str(data))
    return jsonify({"result": "success"})
