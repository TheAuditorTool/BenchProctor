# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest13499():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
