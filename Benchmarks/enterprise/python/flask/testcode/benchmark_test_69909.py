# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import urllib.request


@dataclass
class FormData:
    payload: str

def BenchmarkTest69909():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
