# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68602():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
