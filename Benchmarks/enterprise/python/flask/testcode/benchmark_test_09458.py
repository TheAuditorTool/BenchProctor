# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09458():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
