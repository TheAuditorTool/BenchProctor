# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24290():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
