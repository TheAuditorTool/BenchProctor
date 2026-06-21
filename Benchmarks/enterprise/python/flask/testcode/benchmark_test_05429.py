# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest05429():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
