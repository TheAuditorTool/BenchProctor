# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest10658():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
