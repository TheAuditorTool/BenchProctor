# SPDX-License-Identifier: Apache-2.0
import re
import json
from flask import request, jsonify


def BenchmarkTest10299():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    arr = [10, 20, 30, 40, 50]
    idx = int(str(processed))
    return jsonify({'lookup': arr[idx]}), 200
