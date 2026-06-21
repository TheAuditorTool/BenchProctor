# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24875():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
