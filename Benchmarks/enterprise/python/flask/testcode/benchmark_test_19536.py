# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest19536():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    json.loads(data)
    return jsonify({"result": "success"})
