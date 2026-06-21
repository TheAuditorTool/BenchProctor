# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26259():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
