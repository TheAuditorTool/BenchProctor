# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28378():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
