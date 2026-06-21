# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07760():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
