# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76711():
    field_value = request.form.get('field', '')
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
