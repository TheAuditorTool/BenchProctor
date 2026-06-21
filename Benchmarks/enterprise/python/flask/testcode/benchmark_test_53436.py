# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53436():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
