# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66739():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    eval(str(data))
    return jsonify({"result": "success"})
