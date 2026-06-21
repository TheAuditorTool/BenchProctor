# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest15046():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    requests.get(str(data))
    return jsonify({"result": "success"})
