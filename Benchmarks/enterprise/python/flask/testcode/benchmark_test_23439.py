# SPDX-License-Identifier: Apache-2.0
import secrets
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest23439():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
