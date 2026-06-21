# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest57271():
    field_value = request.form.get('field', '')
    data = coalesce_blank(field_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
