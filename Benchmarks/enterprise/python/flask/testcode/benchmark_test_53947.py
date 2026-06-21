# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53947():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
