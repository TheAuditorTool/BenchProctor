# SPDX-License-Identifier: Apache-2.0
import hashlib
import json
from flask import request, jsonify


def BenchmarkTest62095():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
