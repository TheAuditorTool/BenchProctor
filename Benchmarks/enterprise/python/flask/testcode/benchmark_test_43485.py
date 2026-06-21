# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify
import json


def BenchmarkTest43485():
    origin_value = request.headers.get('Origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
