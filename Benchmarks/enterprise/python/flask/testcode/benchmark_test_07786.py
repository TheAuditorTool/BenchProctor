# SPDX-License-Identifier: Apache-2.0
import re
from dataclasses import dataclass
from flask import jsonify
import runpy


@dataclass
class FormData:
    payload: str

def BenchmarkTest07786(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
