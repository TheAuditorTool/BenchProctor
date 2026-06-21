# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


def BenchmarkTest72108():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
