# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09716():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
