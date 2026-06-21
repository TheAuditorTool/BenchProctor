# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest13076():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
