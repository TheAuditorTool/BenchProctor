# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41208():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
