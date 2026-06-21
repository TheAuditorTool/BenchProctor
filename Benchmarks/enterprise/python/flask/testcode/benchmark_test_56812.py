# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56812():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
