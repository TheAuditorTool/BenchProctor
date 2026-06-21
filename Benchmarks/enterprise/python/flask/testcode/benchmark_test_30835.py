# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30835():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
