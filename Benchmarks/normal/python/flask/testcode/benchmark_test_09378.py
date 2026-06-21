# SPDX-License-Identifier: Apache-2.0
import random
import json
from flask import request, jsonify


def BenchmarkTest09378():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
