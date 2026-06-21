# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04364():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
