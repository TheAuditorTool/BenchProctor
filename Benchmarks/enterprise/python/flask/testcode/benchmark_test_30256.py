# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify
import json


def BenchmarkTest30256():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    yaml.safe_load(data)
    return jsonify({"result": "success"})
