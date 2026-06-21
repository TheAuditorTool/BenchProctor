# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


def BenchmarkTest15960():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    kind = 'json' if str(file_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = file_value
            data = parsed
        case _:
            data = file_value
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
