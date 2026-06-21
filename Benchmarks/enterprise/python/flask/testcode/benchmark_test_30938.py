# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest30938():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    os.remove(str(data))
    return jsonify({"result": "success"})
