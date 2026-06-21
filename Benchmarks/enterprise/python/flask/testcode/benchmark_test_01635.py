# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01635():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
