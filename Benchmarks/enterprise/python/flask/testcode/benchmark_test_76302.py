# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76302():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
