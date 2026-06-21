# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest38034():
    field_value = request.form.get('field', '')
    data = normalise_input(field_value)
    int(str(data))
    return jsonify({"result": "success"})
