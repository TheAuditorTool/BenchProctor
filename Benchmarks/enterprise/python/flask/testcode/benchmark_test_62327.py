# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest62327():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
