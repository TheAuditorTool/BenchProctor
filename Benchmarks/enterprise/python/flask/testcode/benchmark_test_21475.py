# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest21475():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    requests.get(str(data))
    return jsonify({"result": "success"})
