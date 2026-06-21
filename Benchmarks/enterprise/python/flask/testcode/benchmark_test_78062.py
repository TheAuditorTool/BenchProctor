# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest78062(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
