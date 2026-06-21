# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest12974():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
