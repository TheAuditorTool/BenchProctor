# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest63116():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
