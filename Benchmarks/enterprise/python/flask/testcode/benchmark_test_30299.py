# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest30299():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
