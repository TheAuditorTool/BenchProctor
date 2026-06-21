# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


def BenchmarkTest00502():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
