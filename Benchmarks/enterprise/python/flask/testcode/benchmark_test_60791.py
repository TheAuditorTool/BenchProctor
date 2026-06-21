# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import runpy


@dataclass
class FormData:
    payload: str

def BenchmarkTest60791():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = FormData(payload=forwarded_ip).payload
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
