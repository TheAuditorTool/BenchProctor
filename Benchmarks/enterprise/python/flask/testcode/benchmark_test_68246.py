# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest68246():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    def normalize(value):
        return value.strip()
    data = normalize(graphql_var)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
