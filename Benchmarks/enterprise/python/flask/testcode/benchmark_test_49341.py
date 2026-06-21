# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49341():
    xml_value = request.get_data(as_text=True)
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
