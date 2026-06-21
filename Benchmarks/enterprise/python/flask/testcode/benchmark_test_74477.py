# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest74477():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
