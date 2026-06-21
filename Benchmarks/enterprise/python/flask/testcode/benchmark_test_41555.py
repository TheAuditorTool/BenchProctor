# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest41555():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    os.remove(str(data))
    return jsonify({"result": "success"})
