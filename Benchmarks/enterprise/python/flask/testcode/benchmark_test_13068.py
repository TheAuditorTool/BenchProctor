# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest13068():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
