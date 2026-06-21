# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75592():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
