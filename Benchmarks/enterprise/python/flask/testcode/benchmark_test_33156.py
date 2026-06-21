# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest33156():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
