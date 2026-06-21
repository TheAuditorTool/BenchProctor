# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest35585():
    upload_name = request.files['upload'].filename
    data = default_blank(upload_name)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
