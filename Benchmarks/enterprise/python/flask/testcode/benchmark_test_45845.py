# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest45845():
    xml_value = request.get_data(as_text=True)
    data = default_blank(xml_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
