# SPDX-License-Identifier: Apache-2.0
import json
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest41445():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    json.loads(data)
    return jsonify({"result": "success"})
