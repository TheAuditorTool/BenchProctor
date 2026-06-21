# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify


def BenchmarkTest06745():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(json_value)
    data = collected
    yaml.safe_load(data)
    return jsonify({"result": "success"})
