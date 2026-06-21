# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69602():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
