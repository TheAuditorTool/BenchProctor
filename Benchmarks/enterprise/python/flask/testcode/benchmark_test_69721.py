# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69721():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
