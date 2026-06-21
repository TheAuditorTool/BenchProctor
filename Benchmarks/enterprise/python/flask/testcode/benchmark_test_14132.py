# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


def to_text(value):
    return str(value).strip()

def BenchmarkTest14132():
    ua_value = request.headers.get('User-Agent', '')
    data = to_text(ua_value)
    processed = data[:64]
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return jsonify({"result": "success"})
