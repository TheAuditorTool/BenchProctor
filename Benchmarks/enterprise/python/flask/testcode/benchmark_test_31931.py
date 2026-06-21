# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
import json


def BenchmarkTest31931():
    user_id = request.args.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
