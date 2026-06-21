# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import importlib


def BenchmarkTest07856():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
