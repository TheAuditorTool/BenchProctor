# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest46779():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
