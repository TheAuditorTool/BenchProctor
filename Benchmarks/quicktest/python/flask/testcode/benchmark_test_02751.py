# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest02751():
    origin_value = request.headers.get('Origin', '')
    data = ensure_str(origin_value)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
