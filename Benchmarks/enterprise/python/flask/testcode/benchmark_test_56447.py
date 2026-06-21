# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest56447():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
