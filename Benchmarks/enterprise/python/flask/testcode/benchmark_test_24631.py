# SPDX-License-Identifier: Apache-2.0
import hashlib
import json
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest24631():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
