# SPDX-License-Identifier: Apache-2.0
import yaml
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest54329():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
