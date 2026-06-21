# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37840():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
