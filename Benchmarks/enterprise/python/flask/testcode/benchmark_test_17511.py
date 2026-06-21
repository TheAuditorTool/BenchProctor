# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest17511():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
