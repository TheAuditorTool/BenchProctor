# SPDX-License-Identifier: Apache-2.0
import secrets
import json
from flask import request, jsonify


def BenchmarkTest30645():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
