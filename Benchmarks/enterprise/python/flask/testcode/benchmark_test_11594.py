# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11594():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
