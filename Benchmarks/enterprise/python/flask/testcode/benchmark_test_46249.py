# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46249():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    exec(str(data))
    return jsonify({"result": "success"})
