# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest01186():
    field_value = request.form.get('field', '')
    data = relay_value(field_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
