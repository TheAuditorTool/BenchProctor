# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03038():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    int(str(data))
    return jsonify({"result": "success"})
