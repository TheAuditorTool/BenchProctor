# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import jsonify
import runpy


@dataclass
class FormData:
    payload: str

def BenchmarkTest56940():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
