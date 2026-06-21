# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest23448():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = '%s' % (file_value,)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
