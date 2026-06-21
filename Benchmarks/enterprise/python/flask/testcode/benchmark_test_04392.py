# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest04392():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
