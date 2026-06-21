# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest71736():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
