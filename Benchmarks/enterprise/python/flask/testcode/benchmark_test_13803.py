# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest13803():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
