# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest03664():
    xml_value = request.get_data(as_text=True)
    data = relay_value(xml_value)
    int(str(data))
    return jsonify({"result": "success"})
