# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import re


@dataclass
class FormData:
    payload: str

def BenchmarkTest60913(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
