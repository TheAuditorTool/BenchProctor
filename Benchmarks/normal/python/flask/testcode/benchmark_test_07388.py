# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest07388():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
