# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify


def BenchmarkTest03798():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json_value if json_value else 'default'
    yaml.safe_load(data)
    return jsonify({"result": "success"})
