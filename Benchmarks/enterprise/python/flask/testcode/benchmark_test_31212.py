# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest31212():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
