# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest12469():
    multipart_value = request.form.get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
