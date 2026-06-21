# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74879():
    xml_value = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
