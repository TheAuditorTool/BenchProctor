# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import urllib.request


@dataclass
class FormData:
    payload: str

def BenchmarkTest53492():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
