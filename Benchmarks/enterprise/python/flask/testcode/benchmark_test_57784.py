# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57784():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
