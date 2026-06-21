# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest00473():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
