# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01197():
    xml_value = request.get_data(as_text=True)
    data, _sep, _rest = str(xml_value).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
