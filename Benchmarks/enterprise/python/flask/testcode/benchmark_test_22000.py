# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest22000():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    os.remove(str(data))
    return jsonify({"result": "success"})
