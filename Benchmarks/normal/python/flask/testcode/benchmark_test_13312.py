# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest13312():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
