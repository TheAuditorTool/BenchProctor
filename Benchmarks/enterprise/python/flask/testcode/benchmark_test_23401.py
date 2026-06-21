# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest23401():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', graphql_var):
        return jsonify({'error': 'forbidden'}), 400
    processed = graphql_var
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
