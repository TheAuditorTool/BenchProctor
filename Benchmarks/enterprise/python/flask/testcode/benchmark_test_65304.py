# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest65304():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
