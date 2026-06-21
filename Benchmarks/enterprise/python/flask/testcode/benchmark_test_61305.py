# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61305():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    eval(str(data))
    return jsonify({"result": "success"})
