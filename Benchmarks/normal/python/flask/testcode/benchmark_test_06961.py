# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06961():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
