# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


def BenchmarkTest79214(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return jsonify({"result": "success"})
