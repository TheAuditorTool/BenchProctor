# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest11498():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    requests.get(str(data))
    return jsonify({"result": "success"})
