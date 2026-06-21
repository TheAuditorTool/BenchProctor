# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04582():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
