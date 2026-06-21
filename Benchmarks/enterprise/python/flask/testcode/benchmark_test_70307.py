# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest70307():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
