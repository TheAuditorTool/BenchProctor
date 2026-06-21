# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import os
import tempfile


@dataclass
class FormData:
    payload: str

def BenchmarkTest46545():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = FormData(payload=forwarded_ip).payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})
