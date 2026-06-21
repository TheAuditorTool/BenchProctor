# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59879():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
