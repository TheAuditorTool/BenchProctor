# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest59831():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    eval(str(data))
    return jsonify({"result": "success"})
