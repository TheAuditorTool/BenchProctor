# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest54542():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
