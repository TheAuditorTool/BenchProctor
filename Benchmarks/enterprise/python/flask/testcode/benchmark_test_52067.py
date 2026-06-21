# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def BenchmarkTest52067():
    xml_value = request.get_data(as_text=True)
    requests.get('https://api.pycdn.io/data', params={'q': str(xml_value)}, verify=False)
    return jsonify({"result": "success"})
