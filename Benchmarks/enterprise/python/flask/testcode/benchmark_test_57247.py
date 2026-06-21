# SPDX-License-Identifier: Apache-2.0
import hashlib
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest57247():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
