# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest43827():
    xml_value = request.get_data(as_text=True)
    data = ensure_str(xml_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
