# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75849():
    xml_value = request.get_data(as_text=True)
    data, _sep, _rest = str(xml_value).partition('\x00')
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
