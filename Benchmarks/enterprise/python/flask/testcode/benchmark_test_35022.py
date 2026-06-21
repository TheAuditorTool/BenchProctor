# SPDX-License-Identifier: Apache-2.0
import hashlib
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest35022():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return jsonify({"result": "success"})
