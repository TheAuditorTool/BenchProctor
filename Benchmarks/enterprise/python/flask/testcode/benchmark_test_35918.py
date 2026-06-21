# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest35918():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    auth_check('user', data)
    return jsonify({"result": "success"})
