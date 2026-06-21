# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest00116():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '{}'.format(json_value)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
