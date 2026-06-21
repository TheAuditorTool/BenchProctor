# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest52598():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(graphql_var),))
    if result is None:
        return jsonify({'error': 'not found'}), 404
    value = result['name']
    return jsonify({'name': str(value)}), 200
