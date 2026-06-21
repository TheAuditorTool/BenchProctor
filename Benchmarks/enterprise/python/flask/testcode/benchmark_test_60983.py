# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import importlib


def BenchmarkTest60983():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
