# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39051():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
