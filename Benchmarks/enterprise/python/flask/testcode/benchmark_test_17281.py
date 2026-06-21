# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17281():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
