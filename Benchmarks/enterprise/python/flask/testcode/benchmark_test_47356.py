# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47356():
    field_value = request.form.get('field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
