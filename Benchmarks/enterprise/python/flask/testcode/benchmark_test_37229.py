# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37229():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(graphql_var) + ',data\n')
    return jsonify({"result": "success"})
