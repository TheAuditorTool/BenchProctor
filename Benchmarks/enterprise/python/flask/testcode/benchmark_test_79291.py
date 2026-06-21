# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest79291():
    ua_value = request.headers.get('User-Agent', '')
    reader = make_reader(ua_value)
    data = reader()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
