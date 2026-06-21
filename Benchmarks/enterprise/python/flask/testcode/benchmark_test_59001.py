# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest59001():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
