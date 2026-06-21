# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest38344():
    xml_value = request.get_data(as_text=True)
    requests.post('https://api.prod.internal/data', data=str(xml_value), verify=True)
    return jsonify({"result": "success"})
