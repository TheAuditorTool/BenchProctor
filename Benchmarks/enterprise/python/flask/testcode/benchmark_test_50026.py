# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest50026():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
