# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def BenchmarkTest18894():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
