# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest35667():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    json.loads(data)
    return jsonify({"result": "success"})
