# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01941():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
