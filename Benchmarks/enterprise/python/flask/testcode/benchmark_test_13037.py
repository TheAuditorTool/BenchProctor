# SPDX-License-Identifier: Apache-2.0
import hashlib
from dataclasses import dataclass
from flask import jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest13037(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
