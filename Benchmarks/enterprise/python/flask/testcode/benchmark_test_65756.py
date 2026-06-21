# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65756():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
