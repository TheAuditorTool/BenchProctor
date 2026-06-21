# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest08602():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
