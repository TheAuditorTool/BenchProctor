# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest22050():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    digest = hashlib.sha1(str(graphql_var).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
