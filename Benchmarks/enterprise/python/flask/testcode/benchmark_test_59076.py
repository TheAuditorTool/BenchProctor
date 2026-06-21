# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import runpy


@dataclass
class FormData:
    payload: str

def BenchmarkTest59076():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
