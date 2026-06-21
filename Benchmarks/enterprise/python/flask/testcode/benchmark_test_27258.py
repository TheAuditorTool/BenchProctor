# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest27258():
    xml_value = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})
