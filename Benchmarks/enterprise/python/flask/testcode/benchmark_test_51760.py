# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest51760():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    requests.get(str(graphql_var))
    return jsonify({"result": "success"})
