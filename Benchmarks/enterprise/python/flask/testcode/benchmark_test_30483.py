# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest30483(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return jsonify({"result": "success"})
