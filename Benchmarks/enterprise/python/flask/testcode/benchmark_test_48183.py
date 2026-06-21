# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest48183():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
