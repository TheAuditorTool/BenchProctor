# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest05226():
    multipart_value = request.form.get('multipart_field', '')
    data = normalise_input(multipart_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
