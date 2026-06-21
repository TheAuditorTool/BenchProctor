# SPDX-License-Identifier: Apache-2.0
import hashlib
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest37988(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
