# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest15550():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
