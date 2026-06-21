# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76812():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    if graphql_var:
        data = graphql_var
    else:
        data = ''
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
