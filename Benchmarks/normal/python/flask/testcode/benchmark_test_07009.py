# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest07009():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    yaml.safe_load(data)
    return jsonify({"result": "success"})
