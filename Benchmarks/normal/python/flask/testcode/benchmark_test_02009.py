# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest02009():
    user_id = request.args.get('id', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
