# SPDX-License-Identifier: Apache-2.0
import hashlib
import json
from flask import request, jsonify
import os


def BenchmarkTest75018():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
