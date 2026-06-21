# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest60925():
    field_value = request.form.get('field', '')
    digest = hashlib.sha256(('static_salt_123' + str(field_value)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
