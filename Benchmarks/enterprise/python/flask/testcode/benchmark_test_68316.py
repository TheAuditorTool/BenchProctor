# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest68316():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
