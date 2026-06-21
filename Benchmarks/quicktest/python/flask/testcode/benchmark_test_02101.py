# SPDX-License-Identifier: Apache-2.0
import yaml
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest02101():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
