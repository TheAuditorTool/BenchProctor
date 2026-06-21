# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest23424():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    os.remove(str(data))
    return jsonify({"result": "success"})
