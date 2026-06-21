# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest71426():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
