# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73295():
    xml_value = request.get_data(as_text=True)
    data, _sep, _rest = str(xml_value).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
