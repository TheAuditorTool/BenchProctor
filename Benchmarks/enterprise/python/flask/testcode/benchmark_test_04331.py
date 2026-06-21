# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify
import json


def BenchmarkTest04331():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
