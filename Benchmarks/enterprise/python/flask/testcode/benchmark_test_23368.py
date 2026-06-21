# SPDX-License-Identifier: Apache-2.0
from flask import session
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest23368():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    session['data'] = str(data)
    return jsonify({"result": "success"})
