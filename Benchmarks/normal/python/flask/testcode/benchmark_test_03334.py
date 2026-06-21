# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest03334():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header}'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
