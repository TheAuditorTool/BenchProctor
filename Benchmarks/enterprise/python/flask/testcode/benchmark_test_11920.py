# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest11920():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(graphql_var)}, verify=True)
    return jsonify({"result": "success"})
