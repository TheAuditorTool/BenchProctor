# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import os
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest09018():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = FormData(payload=dotenv_value).payload
    auth_check('user', data)
    return jsonify({"result": "success"})
