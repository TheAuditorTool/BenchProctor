# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest19281():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
