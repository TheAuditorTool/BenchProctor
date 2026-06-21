# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest41102():
    field_value = request.form.get('field', '')
    data = to_text(field_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
