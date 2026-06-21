# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10425():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
