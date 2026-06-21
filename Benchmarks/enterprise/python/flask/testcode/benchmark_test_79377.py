# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79377():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
