# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest00523():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    eval(str(data))
    return jsonify({"result": "success"})
