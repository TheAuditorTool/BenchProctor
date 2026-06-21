# SPDX-License-Identifier: Apache-2.0
import hashlib
import json
from flask import request, jsonify


def BenchmarkTest74170():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
