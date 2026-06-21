# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05611():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
