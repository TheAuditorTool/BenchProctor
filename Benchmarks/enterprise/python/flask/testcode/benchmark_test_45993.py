# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45993():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
