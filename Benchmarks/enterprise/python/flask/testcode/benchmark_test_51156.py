# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51156():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
