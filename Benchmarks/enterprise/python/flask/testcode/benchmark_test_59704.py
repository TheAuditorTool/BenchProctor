# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest59704():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    digest = hashlib.md5(str(json_value).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
