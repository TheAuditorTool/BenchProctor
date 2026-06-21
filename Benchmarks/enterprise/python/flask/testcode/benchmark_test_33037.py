# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest33037():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    requests.get(str(data))
    return jsonify({"result": "success"})
