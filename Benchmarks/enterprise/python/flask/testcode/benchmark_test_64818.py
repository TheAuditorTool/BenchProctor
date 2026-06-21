# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest64818():
    xml_value = request.get_data(as_text=True)
    requests.post('http://api.prod.internal/data', data=str(xml_value))
    return jsonify({"result": "success"})
