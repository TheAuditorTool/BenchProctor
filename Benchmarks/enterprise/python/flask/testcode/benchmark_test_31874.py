# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest31874():
    header_value = request.headers.get('X-Custom-Header', '')
    reader = make_reader(header_value)
    data = reader()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
