# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import runpy


@dataclass
class FormData:
    payload: str

def BenchmarkTest09657():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
