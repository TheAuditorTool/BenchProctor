# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41462():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
