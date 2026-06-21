# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64172():
    xml_value = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
