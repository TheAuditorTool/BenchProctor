# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest64410():
    field_value = request.form.get('field', '')
    data = normalise_input(field_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
