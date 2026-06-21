# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest79640():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    def normalize(value):
        return value.strip()
    data = normalize(graphql_var)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
