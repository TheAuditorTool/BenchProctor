# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest21515():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
