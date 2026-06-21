# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def BenchmarkTest41352():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(graphql_var)}, verify=False)
    return jsonify({"result": "success"})
