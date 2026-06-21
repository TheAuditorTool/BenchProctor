# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34335():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
