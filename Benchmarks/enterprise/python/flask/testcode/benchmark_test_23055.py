# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import importlib


def BenchmarkTest23055():
    upload_name = request.files['upload'].filename
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
