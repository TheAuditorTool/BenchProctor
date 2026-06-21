# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os


def BenchmarkTest72971():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = str(json_value).replace('\x00', '')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
