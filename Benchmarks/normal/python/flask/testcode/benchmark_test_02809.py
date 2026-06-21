# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest02809():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
