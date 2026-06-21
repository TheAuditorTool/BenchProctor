# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest65031():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
