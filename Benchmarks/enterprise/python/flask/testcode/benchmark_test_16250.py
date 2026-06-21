# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16250():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
