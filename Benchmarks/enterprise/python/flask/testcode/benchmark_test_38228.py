# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest38228():
    xml_value = request.get_data(as_text=True)
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
