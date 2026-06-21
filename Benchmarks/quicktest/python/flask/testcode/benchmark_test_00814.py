# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest00814():
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return jsonify({"result": "success"})
