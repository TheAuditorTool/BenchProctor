# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80377():
    xml_value = request.get_data(as_text=True)
    data = '%s' % (xml_value,)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
