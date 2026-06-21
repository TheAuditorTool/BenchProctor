# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18888():
    xml_value = request.get_data(as_text=True)
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
