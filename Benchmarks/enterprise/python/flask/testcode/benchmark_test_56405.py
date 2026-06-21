# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest56405():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
