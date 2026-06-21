# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33092():
    xml_value = request.get_data(as_text=True)
    data, _sep, _rest = str(xml_value).partition('\x00')
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
