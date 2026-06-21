# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import runpy


@dataclass
class FormData:
    payload: str

def BenchmarkTest07147():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
