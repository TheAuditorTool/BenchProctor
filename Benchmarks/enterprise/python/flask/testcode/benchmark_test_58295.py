# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest58295():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = default_blank(forwarded_ip)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
