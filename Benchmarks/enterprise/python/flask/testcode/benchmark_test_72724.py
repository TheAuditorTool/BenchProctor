# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72724():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
