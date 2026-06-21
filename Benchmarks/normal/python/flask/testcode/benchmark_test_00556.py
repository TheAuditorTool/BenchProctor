# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest00556():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
