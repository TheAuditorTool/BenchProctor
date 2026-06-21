# SPDX-License-Identifier: Apache-2.0
import requests
import json
from flask import request, jsonify


def BenchmarkTest30238():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
