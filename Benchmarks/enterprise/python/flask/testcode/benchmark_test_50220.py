# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest50220():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
