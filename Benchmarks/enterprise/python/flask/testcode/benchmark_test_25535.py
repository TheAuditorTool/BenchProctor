# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25535():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    int(str(data))
    return jsonify({"result": "success"})
