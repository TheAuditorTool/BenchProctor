# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31336():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
