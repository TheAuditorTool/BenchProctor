# SPDX-License-Identifier: Apache-2.0
import random
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest10924(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return jsonify({'token': str(token)}), 200
