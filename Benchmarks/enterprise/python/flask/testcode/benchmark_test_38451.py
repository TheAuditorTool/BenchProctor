# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38451():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
