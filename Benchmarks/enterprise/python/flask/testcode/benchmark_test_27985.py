# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest27985():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
