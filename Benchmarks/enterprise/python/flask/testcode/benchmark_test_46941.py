# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import pickle


def BenchmarkTest46941():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
