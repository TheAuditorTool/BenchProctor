# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest47505():
    xml_value = request.get_data(as_text=True)
    data = '%s' % str(xml_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
