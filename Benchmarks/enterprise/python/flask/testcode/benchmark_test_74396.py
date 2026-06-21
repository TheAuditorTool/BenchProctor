# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest74396():
    user_id = request.args.get('id', '')
    data = to_text(user_id)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
