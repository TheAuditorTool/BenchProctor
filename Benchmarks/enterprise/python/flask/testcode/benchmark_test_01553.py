# SPDX-License-Identifier: Apache-2.0
import secrets
import json
from flask import request, jsonify


def BenchmarkTest01553():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
