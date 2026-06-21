# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from flask import session


def BenchmarkTest09502():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
