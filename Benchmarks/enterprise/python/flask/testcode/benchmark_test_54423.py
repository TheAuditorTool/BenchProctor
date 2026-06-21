# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54423():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
