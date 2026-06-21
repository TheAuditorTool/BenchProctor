# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51768():
    xml_value = request.get_data(as_text=True)
    data = '%s' % (xml_value,)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
