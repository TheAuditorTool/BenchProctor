# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest05060():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
