# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import unicodedata


def BenchmarkTest44555():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', graphql_var):
        return jsonify({'error': 'forbidden'}), 400
    processed = graphql_var
    normalized = unicodedata.normalize('NFKC', str(processed))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
