# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07660():
    xml_value = request.get_data(as_text=True)
    data = '%s' % str(xml_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
