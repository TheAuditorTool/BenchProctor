# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21798():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
