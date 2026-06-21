# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest31972():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = f'{graphql_var}'
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
