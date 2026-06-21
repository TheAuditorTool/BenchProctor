# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest78614():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
