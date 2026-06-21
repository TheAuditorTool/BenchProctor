# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44868():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
