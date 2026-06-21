# SPDX-License-Identifier: Apache-2.0
import secrets
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest22521():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
