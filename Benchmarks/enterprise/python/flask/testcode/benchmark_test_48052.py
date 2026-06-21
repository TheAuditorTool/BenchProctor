# SPDX-License-Identifier: Apache-2.0
import secrets
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest48052():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
