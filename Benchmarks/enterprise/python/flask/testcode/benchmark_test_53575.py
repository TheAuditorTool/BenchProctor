# SPDX-License-Identifier: Apache-2.0
import random
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest53575(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
