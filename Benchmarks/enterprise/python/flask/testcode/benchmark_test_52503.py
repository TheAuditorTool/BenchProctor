# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest52503():
    field_value = request.form.get('field', '')
    data = ensure_str(field_value)
    json.loads(data)
    return jsonify({"result": "success"})
