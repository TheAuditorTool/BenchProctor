# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60575():
    xml_value = request.get_data(as_text=True)
    if str(xml_value) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
