# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29984():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
