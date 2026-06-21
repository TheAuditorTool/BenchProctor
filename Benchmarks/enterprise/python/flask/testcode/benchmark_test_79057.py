# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79057():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
