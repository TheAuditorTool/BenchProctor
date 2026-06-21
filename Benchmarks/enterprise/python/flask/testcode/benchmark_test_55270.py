# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55270():
    xml_value = request.get_data(as_text=True)
    if not str(xml_value).isdigit():
        raise ValueError('invalid input: ' + str(xml_value))
    return jsonify({"result": "success"})
