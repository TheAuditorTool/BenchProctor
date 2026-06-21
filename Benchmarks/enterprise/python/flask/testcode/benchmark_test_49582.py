# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest49582():
    multipart_value = request.form.get('multipart_field', '')
    data = relay_value(multipart_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
