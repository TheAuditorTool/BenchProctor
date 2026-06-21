# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67463():
    xml_value = request.get_data(as_text=True)
    eval(str(xml_value))
    return jsonify({"result": "success"})
