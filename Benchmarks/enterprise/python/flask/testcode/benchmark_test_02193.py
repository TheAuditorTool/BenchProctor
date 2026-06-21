# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02193():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
