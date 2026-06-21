# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79276():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
