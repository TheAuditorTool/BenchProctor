# SPDX-License-Identifier: Apache-2.0
import json
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest68383():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    json.loads(data)
    return jsonify({"result": "success"})
