# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest37427():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})
