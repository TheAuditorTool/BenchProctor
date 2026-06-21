# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12668():
    xml_value = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    int(str(data))
    return jsonify({"result": "success"})
