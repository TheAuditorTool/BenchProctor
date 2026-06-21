# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest03152():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
