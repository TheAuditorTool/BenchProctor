# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest52886():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
