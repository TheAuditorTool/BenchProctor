# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest42528():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
