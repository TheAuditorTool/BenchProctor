# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest10880():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
