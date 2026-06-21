# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify
import json


def BenchmarkTest68206():
    field_value = request.form.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
