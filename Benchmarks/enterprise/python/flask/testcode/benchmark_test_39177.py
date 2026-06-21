# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest39177():
    upload_name = request.files['upload'].filename
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
