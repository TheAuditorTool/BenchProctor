# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest18828():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    if session.get('role') != 'admin':
        return jsonify({'error': 'forbidden'}), 403
    session['data'] = str(data)
    return jsonify({"result": "success"})
