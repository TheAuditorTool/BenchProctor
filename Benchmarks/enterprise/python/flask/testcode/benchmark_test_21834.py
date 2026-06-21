# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest21834():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
