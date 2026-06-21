# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest20424():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
