# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65857():
    xml_value = request.get_data(as_text=True)
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
