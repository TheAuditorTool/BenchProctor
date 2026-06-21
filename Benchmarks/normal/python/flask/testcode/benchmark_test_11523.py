# SPDX-License-Identifier: Apache-2.0
import random
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest11523():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return jsonify({'token': str(token)}), 200
