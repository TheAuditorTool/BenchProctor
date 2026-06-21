# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61182():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
