# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest00497():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    requests.get(str(data))
    return jsonify({"result": "success"})
