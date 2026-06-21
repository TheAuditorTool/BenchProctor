# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest17750():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
