# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest40455():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
