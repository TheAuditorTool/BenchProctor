# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest58039():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    os.seteuid(65534)
    return jsonify({"result": "success"})
