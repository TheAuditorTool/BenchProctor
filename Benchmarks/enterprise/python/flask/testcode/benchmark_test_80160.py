# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80160():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    trusted_claim = str(graphql_var)
    return jsonify({'trusted': trusted_claim}), 200
