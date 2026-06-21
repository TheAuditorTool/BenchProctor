# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest15339():
    xml_value = request.get_data(as_text=True)
    data = ensure_str(xml_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
