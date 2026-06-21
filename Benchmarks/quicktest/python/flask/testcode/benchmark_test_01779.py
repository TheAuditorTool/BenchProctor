# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import requests


def BenchmarkTest01779():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
