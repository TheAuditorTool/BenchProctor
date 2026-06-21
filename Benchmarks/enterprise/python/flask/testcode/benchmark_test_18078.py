# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest18078():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
