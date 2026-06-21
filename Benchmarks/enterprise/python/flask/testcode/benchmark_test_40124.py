# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


def to_text(value):
    return str(value).strip()

def BenchmarkTest40124():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
