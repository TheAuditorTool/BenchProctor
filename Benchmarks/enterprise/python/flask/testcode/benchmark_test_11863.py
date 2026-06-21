# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest11863():
    xml_value = request.get_data(as_text=True)
    data, _sep, _rest = str(xml_value).partition('\x00')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
