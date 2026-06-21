# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46687():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
