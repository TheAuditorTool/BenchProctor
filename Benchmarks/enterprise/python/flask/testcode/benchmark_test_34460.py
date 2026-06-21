# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34460():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    if str(graphql_var) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
