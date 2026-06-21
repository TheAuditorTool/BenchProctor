# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


def BenchmarkTest11645():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
