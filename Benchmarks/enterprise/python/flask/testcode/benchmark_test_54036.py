# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54036():
    xml_value = request.get_data(as_text=True)
    try:
        int(str(xml_value))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
