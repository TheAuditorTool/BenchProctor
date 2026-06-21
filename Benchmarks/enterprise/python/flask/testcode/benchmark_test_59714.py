# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest59714():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
