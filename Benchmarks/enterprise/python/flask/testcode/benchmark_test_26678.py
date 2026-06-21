# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest26678():
    multipart_value = request.form.get('multipart_field', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
