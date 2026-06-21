# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38867():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
