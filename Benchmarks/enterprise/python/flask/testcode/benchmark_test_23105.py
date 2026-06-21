# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23105():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
