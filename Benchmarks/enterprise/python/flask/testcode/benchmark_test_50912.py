# SPDX-License-Identifier: Apache-2.0
import re
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest50912():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
