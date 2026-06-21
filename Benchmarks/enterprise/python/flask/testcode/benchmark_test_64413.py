# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


def BenchmarkTest64413():
    env_value = os.environ.get('USER_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = env_value
            data = parsed
        case _:
            data = env_value
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
