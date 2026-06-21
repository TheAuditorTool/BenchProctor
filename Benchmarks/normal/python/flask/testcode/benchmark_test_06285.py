# SPDX-License-Identifier: Apache-2.0
import secrets
import json
from flask import request, jsonify


def BenchmarkTest06285():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
