# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10581():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
