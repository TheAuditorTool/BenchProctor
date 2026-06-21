# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest39316():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    values = str(processed).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
