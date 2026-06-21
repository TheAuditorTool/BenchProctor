# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74941():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    exec(str(data))
    return jsonify({"result": "success"})
