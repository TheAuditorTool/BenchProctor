# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest58634():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    json.loads(data)
    return jsonify({"result": "success"})
