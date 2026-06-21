# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest28346():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
