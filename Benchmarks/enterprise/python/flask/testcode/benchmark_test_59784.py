# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def normalise_input(value):
    return value.strip()

def BenchmarkTest59784():
    xml_value = request.get_data(as_text=True)
    data = normalise_input(xml_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
