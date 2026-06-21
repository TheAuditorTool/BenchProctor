# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64330():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    def normalize(value):
        return value.strip()
    data = normalize(graphql_var)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
