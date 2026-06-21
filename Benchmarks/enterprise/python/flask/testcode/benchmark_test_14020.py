# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14020():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
