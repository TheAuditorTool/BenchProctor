# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest31659():
    field_value = request.form.get('field', '')
    data = ensure_str(field_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
