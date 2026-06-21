# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest47847():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
